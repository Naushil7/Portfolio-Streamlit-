import streamlit as st
import os
import base64

def st_all():
    # Define the path to your resume file, which is outside the 'tabs' folder
    resume_path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'resume.pdf')

    try:
        # Read the resume PDF file as bytes
        with open(resume_path, "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        # Encode the PDF to base64 for embedding
        base64_pdf = base64.b64encode(PDFbyte).decode('utf-8')

        # Embed the PDF file using an iframe, centered and with adjusted width/height
        pdf_display = f'''
        <div style="display: flex; justify-content: center;">
            <iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="1200px" style="border: none;"></iframe>
        </div>
        '''
        st.markdown(pdf_display, unsafe_allow_html=True)
        
        # Center the download button
        st.markdown(
            "<div style='text-align: center; margin-top: 20px;'>",
            unsafe_allow_html=True,
        )
        st.markdown("</div>", unsafe_allow_html=True)

    except FileNotFoundError:
        st.error("Resume file not found. Please ensure the path is correct.")
