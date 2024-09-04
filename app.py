import streamlit as st
from tabs import home, resume, projects, contact

def main():
    st.set_page_config(
        page_icon=':chart_with_upwards_trend:',
        page_title='Naushil Khajanchi',
        layout='wide',
    )

    # Custom CSS for Dark Theme with Neon Colors and Tabular Effect
    st.markdown("""
        <style>
        /* Remove the background color of the main content area */
        .block-container {
            padding-top: 1rem !important;
            padding-left: 2rem !important;
            padding-right: 2rem !important;
            background-color: transparent !important;
        }

        /* Remove the background color of the sidebar (if used) */
        .sidebar .sidebar-content {
            background-color: transparent !important;
        }

        /* Set the body's background to match the theme or be completely seamless */
        body {
            background-color: #1e1e1e !important; /* Or set to transparent for a completely seamless window */
        }
        /* Main container padding */
        .block-container {
            padding-top: 1rem !important;
            padding-left: 2rem !important;
            padding-right: 2rem !important;
            background-color: #1e1e1e;
            color: #ffffff;
        }

        /* Title styling */
        h1 {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            font-size: 3rem;
            text-align: center;
            margin-bottom: 1.5rem;
            color: #ffffff; /* White */
            text-shadow: 0 0 10px #ffffff;
        }
    
        /* Centering content */
        .center-content {
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            text-align: center;
        }

        /* Styling for the tabular-box */
        .tabular-box {
            background-color: rgba(46, 46, 46, 0.5); /* Slightly transparent */
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            transition: transform 0.2s, box-shadow 0.2s;
            text-align: left;
            color: #ffffff;
        }

        .tabular-box:hover {
            transform: scale(1.02);
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
        }

        /* Button styling within the tabular-box */
        .tabular-box .button {
            display: inline-block;
            background-color: #0077B5;
            color: #ffffff;
            padding: 8px 16px;
            margin-top: 10px;
            border-radius: 8px;
            text-decoration: none;
            font-weight: bold;
            transition: background-color 0.3s ease;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        .tabular-box .button:hover {
            background-color: #005a8c;
        }

        /* Button styling */
        .stButton button {
            background-color: #ffffff;
            color: #1e1e1e;
            border: none;
            padding: 10px 24px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 8px;
            transition: background-color 0.3s ease, transform 0.3s ease;
            box-shadow: 0 0 10px #ffffff;
        }

        /* Button hover effect */
        .stButton button:hover {
            background-color: #2e8b57; /* Darker shade */
            transform: translateY(-2px);
            color: #ffffff;
        }

        /* Navigation Tabs */
        .stTabs [role="tablist"] > [role="tab"] {
            color: #ffffff;
            font-size: 1.1rem;
            transition: color 0.3s ease;
        }

        .stTabs [role="tablist"] > [role="tab"][aria-selected="true"] {
            color: #ffffff;
            border-bottom: 2px solid #ffffff;
        }

        /* Animation for the sections */
        .section {
            animation: fadeInUp 0.5s ease-in-out;
        }

        @keyframes fadeInUp {
            0% {
                opacity: 0;
                transform: translateY(20px);
            }
            100% {
                opacity: 1;
                transform: translateY(0);
            }
        }

        /* Styling for links */
        a {
            color: #ffffff;
            text-decoration: none;
        }

        a:hover {
            color: #ffffff;
            text-shadow: 0 0 5px #ffffff;
        }

        </style>
    """, unsafe_allow_html=True)

    # Layout
    left_col, main_col, right_col = st.columns([1, 2, 1])

    with main_col:
        st.title('Naushil Khajanchi')
        st.markdown(
            '''
            <div style="text-align: center;">
                <a href="mailto:nkhajanc@usc.edu"><img src="https://img.shields.io/badge/-nkhajanc@usc.edu-181717?style=flat-square&logo=gmail&logoColor=white" alt="GitHub"></a> |
                <a href="https://www.linkedin.com/in/naushilkhajanchi/">
                    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn">
                </a> |
                <a href="https://github.com/Naushil7">
                    <img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white" alt="GitHub">
                </a>
            </div>
            ''',
            unsafe_allow_html=True
        )

        # Tabs for navigation
        tabs = st.tabs(["Home", "Resume", "Projects", "Contact"])
        
        with tabs[0]:
            home.st_all()  # Assuming `home` module exists

        with tabs[1]:
            st.markdown('<div class="center-content">', unsafe_allow_html=True)
            resume.st_all()  # Centering the resume content
            st.markdown('</div>', unsafe_allow_html=True)


        with tabs[2]:
            projects.st_all()  # This function displays projects

        with tabs[3]:
            contact.st_all()  # This function displays the contact information

if __name__ == "__main__":
    main()
