import streamlit as st
import os

def st_all():
    # Define the path to your README.md file using a relative path
    readme_path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'readme.md')

    try:
        # Read the content of the README.md file
        with open(readme_path, 'r', encoding='utf-8') as file:
            readme_content = file.read()

        # Render the README.md content in the Streamlit app
        st.markdown(readme_content, unsafe_allow_html=True)
    except FileNotFoundError:
        st.error("README.md file not found. Please ensure the path is correct.")

