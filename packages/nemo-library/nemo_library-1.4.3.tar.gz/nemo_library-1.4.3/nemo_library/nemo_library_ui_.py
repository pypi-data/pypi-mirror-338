import tempfile
import streamlit as st
from nemo_library.utils.config import Config
from streamlit_option_menu import option_menu  # Add this import
import json
import os
from nemo_library.nemo_library import NemoLibrary
import logging  # Add logging import
import threading  # Add threading import
import time  # Add time import
from datetime import datetime  # Add this import

st.header("User Interface for NEMO Library")
st.subheader("Interactive User Interface for NEMO Library")
st.markdown(
    "This is a user interface for the NEMO library, allowing users to interact with NEMO's functionalities."
)

# Load profiles from persistent storage
from cryptography.fernet import Fernet

# Generate a valid encryption key (only needs to be done once)
# encryption_key = Fernet.generate_key().decode()  # Uncomment to generate a new key
# print(encryption_key)

# Use a valid encryption key
config = Config(encryption_key="UBGPjeK9i2nl_809ofmRbXsW3Ok5JFhZs9bfrLpyyVA=")
profiles_file = "profiles.json"
selected_profile_file = "selected_profile.json"

# Load profiles using Config's load_profiles method
profiles = config.load_profiles(profiles_file)

# Load the selected profile from persistent storage
if os.path.exists(selected_profile_file):
    with open(selected_profile_file, "r") as f:
        st.session_state["selected_profile"] = json.load(f).get(
            "selected_profile", "None"
        )
else:
    st.session_state["selected_profile"] = "None"


def getNL() -> NemoLibrary:
    """
    Get the NemoLibrary instance for the given profile name.
    """
    profile_name = st.session_state.get("selected_profile", "None")
    if profile_name in profiles:
        return NemoLibrary(
            encryption_key="UBGPjeK9i2nl_809ofmRbXsW3Ok5JFhZs9bfrLpyyVA=",
            tenant=profiles[profile_name]["tenant"],
            userid=profiles[profile_name]["userid"],
            password=profiles[profile_name]["password"],
            environment=profiles[profile_name]["environment"],
            hubspot_api_token=profiles[profile_name].get("hubspot_api_token"),
            migman_local_project_directory=profiles[profile_name].get(
                "migman_local_project_directory"
            ),
            migman_proALPHA_project_status_file=profiles[profile_name].get(
                "migman_proALPHA_project_status_file"
            ),
            migman_projects=profiles[profile_name].get("migman_projects", []),
            migman_mapping_fields=profiles[profile_name].get(
                "migman_mapping_fields", []
            ),
            migman_additional_fields=profiles[profile_name].get(
                "migman_additional_fields", {}
            ),
            migman_multi_projects=profiles[profile_name].get(
                "migman_multi_projects", {}
            ),
        )


def real_time_logging(streamlit_logger, method, *args):
    success_placeholder = st.empty()  # Placeholder for success or error messages
    log_placeholder = st.empty()  # Placeholder for real-time logs
    try:
        # Call the method with the temporary file path
        def process_rules():
            with st.spinner("Processing..."):
                method(*args)

        # Start the processing in a separate thread
        processing_thread = threading.Thread(target=process_rules)
        processing_thread.start()

        # Update logs in the main thread
        while processing_thread.is_alive():
            log_placeholder.text_area(
                "Logs",
                "\n".join(streamlit_logger.logs),
                height=300,
                key=f"log_box_{datetime.now().timestamp()}",  # Use a unique key
            )
            time.sleep(0.5)  # Update logs every 0.5 seconds

            # Wait for the processing thread to finish
        processing_thread.join()

        # Show success message after logs are displayed
        success_placeholder.success("Rules created or updated successfully!")

        # Display final logs
        log_placeholder.text_area(
            "Logs",
            "\n".join(streamlit_logger.logs),
            height=300,
            key=f"log_box_{datetime.now().timestamp()}",  # Use a unique key
        )

    except Exception as e:
        success_placeholder.error(f"An error occurred: {e}")


class StreamlitLoggerHandler(logging.Handler):
    """
    Custom logging handler to capture logs and display them in Streamlit.
    """

    def __init__(self):
        super().__init__()
        self.logs = []

    def emit(self, record):
        self.logs.append(self.format(record))


# Initialize the custom logger handler
streamlit_logger = StreamlitLoggerHandler()
streamlit_logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
streamlit_logger.setFormatter(formatter)
logging.getLogger().addHandler(streamlit_logger)
logging.getLogger().setLevel(logging.INFO)

# Sidebar navigation using option_menu
with st.sidebar:
    st.markdown(f"**Version:** {NemoLibrary.get_version()}")  # Display version in the sidebar
    menu = option_menu(
        "Menu",
        ["Nemo Library", "Settings"],
        icons=["house", "gear"],  # Add icons for better UI
        menu_icon="menu-app",  # Icon for the menu
        default_index=0,  # Default selected menu
    )

    if menu == "Nemo Library":
        sub_menu = option_menu(
            "Nemo Library",
            ["Projects", "Deficiency Mining"],
            icons=["folder", "check-circle"],
            menu_icon="list",
            default_index=0,
        )

    # Display the selected profile at the top of the sidebar
    selected_profile = st.sidebar.selectbox(
        "Select Profile",
        ["None"] + list(profiles.keys()),
        index=(["None"] + list(profiles.keys())).index(
            st.session_state.get("selected_profile", "None")
        ),
    )
    st.session_state["selected_profile"] = selected_profile


if menu == "Nemo Library" and sub_menu == "Projects":
    st.header("Projects")
    tabs = st.tabs(
        ["Project List", "Update Project"]
    )  # Create tabs for different functionalities
    with tabs[0]:
        nl = getNL()
        projects = nl.getProjects()

        # Display projects in a grid control
        if projects:
            # Assuming projects is a list of dictionaries
            st.dataframe(
                projects, use_container_width=True, height=600
            )  # Display as a grid with max width and custom height
        else:
            st.write("No projects found.")
    with tabs[1]:
        nl = getNL()  # Ensure NemoLibrary instance is available
        project_list = nl.getProjects()  # Fetch the list of projects
        selected_project = st.selectbox(
            "Select a Project", 
            options=[project.displayName for project in project_list] if project_list else ["No projects available"]
        )  # Combo box to select a project

        uploaded_file = st.file_uploader(
            "Upload File (CSV format)",
            type=["csv"],
            accept_multiple_files=False,
        )  # File uploader for XLSX files
        if st.button(
            "Create or Update Rules", disabled=not uploaded_file
        ):  # Disable button if no file is uploaded
            if uploaded_file:
                try:
                    # Save the uploaded file temporarily
                    with tempfile.TemporaryDirectory() as temp_dir:
                        temp_file_path = os.path.join(temp_dir, "tempfile.csv")

                        with open(temp_file_path, "wb") as temp_file:
                            temp_file.write(uploaded_file.getbuffer())

                        nl = getNL()
                        real_time_logging(
                            streamlit_logger,
                            nl.ReUploadFile,
                            temp_file_path,
                        )

                except Exception as e:
                    st.error(f"An error occurred: {e}")
            else:
                st.error("Please upload a valid XLSX file.")
elif menu == "Nemo Library" and sub_menu == "Deficiency Mining":
    st.header("Deficiency Mining")
    st.subheader("Create or Update Rules by Config File")
    uploaded_file = st.file_uploader(
        "Upload Config File (XLSX format)",
        type=["xlsx", "xls", "csv"],
        accept_multiple_files=False,
    )  # File uploader for XLSX files
    if st.button(
        "Create or Update Rules", disabled=not uploaded_file
    ):  # Disable button if no file is uploaded
        if uploaded_file:
            try:
                # Save the uploaded file temporarily
                with tempfile.TemporaryDirectory() as temp_dir:
                    temp_file_path = os.path.join(temp_dir, "tempfile.csv")

                    with open(temp_file_path, "wb") as temp_file:
                        temp_file.write(uploaded_file.getbuffer())

                    nl = getNL()
                    real_time_logging(
                        streamlit_logger,
                        nl.createOrUpdateRulesByConfigFile,
                        temp_file_path,
                    )

            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.error("Please upload a valid XLSX file.")
    # Add logic for Projects here
elif menu == "Settings":
    st.subheader("Profile Management")
    selected_profile_option = st.selectbox(
        "Select Profile", ["Create New"] + list(profiles.keys())
    )

    if selected_profile_option == "Create New":
        if st.button("Save Profile"):
            new_profile_name = st.session_state.get("new_profile_name")
            if new_profile_name and new_profile_name not in profiles:
                profiles[new_profile_name] = {
                    "tenant": st.session_state.get("new_tenant"),
                    "userid": st.session_state.get("new_userid"),
                    "password": st.session_state.get("new_password"),
                    "environment": st.session_state.get("new_environment"),
                    "hubspot_api_token": st.session_state.get("new_hubspot_api_token"),
                    "migman_local_project_directory": st.session_state.get(
                        "new_migman_local_project_directory"
                    ),
                    "migman_proALPHA_project_status_file": st.session_state.get(
                        "new_migman_proALPHA_project_status_file"
                    ),
                    "migman_projects": st.session_state.get(
                        "new_migman_projects", ""
                    ).split(","),
                    "migman_mapping_fields": st.session_state.get(
                        "new_migman_mapping_fields", ""
                    ).split(","),
                    "migman_additional_fields": json.loads(
                        st.session_state.get("new_migman_additional_fields", "{}")
                        or "{}"
                    ),
                    "migman_multi_projects": json.loads(
                        st.session_state.get("new_migman_multi_projects", "{}") or "{}"
                    ),
                    "metadata": st.session_state.get("new_metadata"),
                }
                config.save_profiles(profiles, profiles_file)
                st.session_state["selected_profile"] = new_profile_name
                # Save the selected profile to persistent storage
                with open(selected_profile_file, "w") as f:
                    json.dump({"selected_profile": new_profile_name}, f)
                st.success(f"Profile '{new_profile_name}' created successfully!")
            else:
                st.error("Profile name is required or already exists.")
        st.text_input("Profile Name", key="new_profile_name")
        st.text_input("Tenant", key="new_tenant")
        st.text_input("User ID", key="new_userid")
        st.text_input("Password", key="new_password", type="password")
        st.text_input("Environment", key="new_environment")
        st.text_input("HubSpot API Token", key="new_hubspot_api_token", type="password")
        st.text_input(
            "migman_local_project_directory", key="new_migman_local_project_directory"
        )
        st.text_input(
            "migman_proALPHA_project_status_file",
            key="new_migman_proALPHA_project_status_file",
        )
        st.text_area("migman_projects (comma-separated)", key="new_migman_projects")
        st.text_area(
            "migman_mapping_fields (comma-separated)", key="new_migman_mapping_fields"
        )
        st.text_area(
            "migman_additional_fields (JSON format)", key="new_migman_additional_fields"
        )
        st.text_area(
            "migman_multi_projects (JSON format)", key="new_migman_multi_projects"
        )
        st.text_input("metadata", key="new_metadata")
    else:
        if st.button("Update Profile"):
            profiles[selected_profile_option] = {
                "tenant": st.session_state.get("edit_tenant"),
                "userid": st.session_state.get("edit_userid"),
                "password": st.session_state.get("edit_password"),
                "environment": st.session_state.get("edit_environment"),
                "hubspot_api_token": st.session_state.get("edit_hubspot_api_token"),
                "migman_local_project_directory": st.session_state.get(
                    "edit_migman_local_project_directory"
                ),
                "migman_proALPHA_project_status_file": st.session_state.get(
                    "edit_migman_proALPHA_project_status_file"
                ),
                "migman_projects": st.session_state.get(
                    "edit_migman_projects", ""
                ).split(","),
                "migman_mapping_fields": st.session_state.get(
                    "edit_migman_mapping_fields", ""
                ).split(","),
                "migman_additional_fields": json.loads(
                    st.session_state.get("edit_migman_additional_fields", "{}") or "{}"
                ),
                "migman_multi_projects": json.loads(
                    st.session_state.get("edit_migman_multi_projects", "{}") or "{}"
                ),
                "metadata": st.session_state.get("edit_metadata"),
            }
            config.save_profiles(profiles, profiles_file)
            st.success(f"Profile '{selected_profile_option}' updated successfully!")
        if st.button("Delete Profile"):
            del profiles[selected_profile_option]
            config.save_profiles(profiles, profiles_file)
            st.session_state["selected_profile"] = "None"
            # Save the updated selected profile to persistent storage
            with open(selected_profile_file, "w") as f:
                json.dump({"selected_profile": "None"}, f)
            st.success(f"Profile '{selected_profile_option}' deleted successfully!")

        st.session_state["selected_profile"] = selected_profile_option
        # Save the selected profile to persistent storage
        with open(selected_profile_file, "w") as f:
            json.dump({"selected_profile": selected_profile_option}, f)
        profile_data = profiles[selected_profile_option]
        st.text_input("Tenant", value=profile_data["tenant"], key="edit_tenant")
        st.text_input("User ID", value=profile_data["userid"], key="edit_userid")
        st.text_input(
            "Password",
            value=profile_data["password"],
            type="password",
            key="edit_password",
        )
        st.text_input(
            "Environment", value=profile_data["environment"], key="edit_environment"
        )
        st.text_input(
            "HubSpot API Token",
            value=profile_data["hubspot_api_token"],
            type="password",
            key="edit_hubspot_api_token",
        )
        st.text_input(
            "migman_local_project_directory",
            value=profile_data.get("migman_local_project_directory", ""),
            key="edit_migman_local_project_directory",
        )
        st.text_input(
            "migman_proALPHA_project_status_file",
            value=profile_data.get("migman_proALPHA_project_status_file", ""),
            key="edit_migman_proALPHA_project_status_file",
        )
        st.text_area(
            "migman_projects (comma-separated)",
            value=",".join(profile_data.get("migman_projects", [])),
            key="edit_migman_projects",
        )
        st.text_area(
            "migman_mapping_fields (comma-separated)",
            value=",".join(profile_data.get("migman_mapping_fields", [])),
            key="edit_migman_mapping_fields",
        )
        st.text_area(
            "migman_additional_fields (JSON format)",
            value=json.dumps(profile_data.get("migman_additional_fields", {})),
            key="edit_migman_additional_fields",
        )
        st.text_area(
            "migman_multi_projects (JSON format)",
            value=json.dumps(profile_data.get("migman_multi_projects", {})),
            key="edit_migman_multi_projects",
        )
        st.text_input(
            "metadata", value=profile_data.get("metadata", ""), key="edit_metadata"
        )
