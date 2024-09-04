import streamlit as st

def st_all():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.markdown("<h2>Contact Me</h2>", unsafe_allow_html=True)
    st.markdown("<p>Feel free to reach out to me via email or social media. I'm always open to discussing new projects, creative ideas, or opportunities to be part of your visions.</p>", unsafe_allow_html=True)
    
    st.markdown(
        '''
        <p>
            📧 <a href="mailto:nkhajanc@usc.edu">nkhajanc@usc.edu</a><br>
            🌐 <a href="https://www.linkedin.com/in/naushilkhajanchi/" target="_blank">LinkedIn</a><br>
            🐙 <a href="https://github.com/Naushil7" target="_blank">GitHub</a>
        </p>
        ''',
        unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)
