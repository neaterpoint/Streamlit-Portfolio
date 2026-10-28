import streamlit as st

st.set_page_config(
    page_title="Vince Mathew L. Silva | Portfolio",
    page_icon="👋",
    layout="wide",
)

page = st.navigation(
    [
        st.Page("pages/home.py", title="Home", icon=":material/home:"),
        st.Page("pages/about.py", title="About", icon=":material/person:"),
        st.Page("pages/contact.py", title="Contact", icon=":material/phone:"),
    ],
    position="top", 
)

page.run()