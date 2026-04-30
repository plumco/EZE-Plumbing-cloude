import streamlit as st
import streamlit.components.v1 as components

# Make the Streamlit page take up the full screen width
st.set_page_config(layout="wide", page_title="BOQ Builder")

# Hide Streamlit's default header, footer, and blank padding
st.markdown("""
    <style>
        /* Remove blank space at the top, bottom, and sides */
        .block-container {
            padding-top: 0rem;
            padding-bottom: 0rem;
            padding-left: 0rem;
            padding-right: 0rem;
            max-width: 100%;
        }
        /* Hide the top menu bar and bottom footer */
        header {visibility: hidden;}
        footer {visibility: hidden;}
        
        /* Optional: hide the "Deploy" button specifically */
        .stAppDeployButton {display: none;}
    </style>
    """, unsafe_allow_html=True)

# Try to read your HTML file and display it
try:
    with open("boq.html", "r", encoding="utf-8") as f:
        html_data = f.read()

    # Render the HTML inside Streamlit. 
    # Height is set to 800 to give it plenty of room.
    components.html(html_data, height=800, scrolling=True)

except FileNotFoundError:
    st.error("❌ Error: Could not find 'boq.html'. Please make sure your HTML file is uploaded to this GitHub repository and is named exactly 'boq.html' (all lowercase).")
