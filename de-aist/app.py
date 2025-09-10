import streamlit as st
import streamlit.components.v1 as components
import os

# Set Streamlit page configuration
st.set_page_config(
    page_title="AI 팝업 스튜디오 웹페이지",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- Configuration for multiple HTML pages ---
# Define the base directory for HTML files
HTML_DIR = os.path.join(os.path.dirname(__file__), "htmls")

# Find all 'index.html' files in the htmls directory and its subdirectories
# Map them to user-friendly names for the sidebar menu
pages = {}
if os.path.exists(HTML_DIR):
    for root, dirs, files in os.walk(HTML_DIR):
        if "index.html" in files:
            # Create a relative path from the HTML_DIR
            rel_path = os.path.relpath(root, HTML_DIR)
            
            # Create a user-friendly name for the page
            if rel_path == ".":
                page_name = "메인 페이지"
            else:
                page_name = f"페이지: {rel_path}"
            
            # Store the full path with the page name
            pages[page_name] = os.path.join(root, "index.html")

# --- Page Selection in Sidebar ---
# If no HTML files are found, show an error
if not pages:
    st.error(f"HTML 파일을 찾을 수 없습니다: {HTML_DIR}")
else:
    # Use a radio button in the sidebar to select the page
    selected_page_name = st.sidebar.radio("페이지를 선택하세요:", list(pages.keys()))
    
    # Get the selected file path
    selected_file_path = pages[selected_page_name]

    # --- HTML File Loading and Rendering ---
    if not os.path.exists(selected_file_path):
        st.error(f"선택한 HTML 파일을 찾을 수 없습니다: {selected_file_path}")
    else:
        # Read the selected HTML file
        with open(selected_file_path, "r", encoding="utf-8") as f:
            html_code = f.read()

        # Render the HTML code in Streamlit
        components.html(html_code, height=1000, scrolling=True)

# Add simple styling to the bottom of the page (optional)
st.markdown("""
<style>
    .streamlit-container {
        padding-top: 0;
    }
</style>
""", unsafe_allow_html=True)
