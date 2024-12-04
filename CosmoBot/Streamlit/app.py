import streamlit as st

# Define your pages as before
CosmoBotpage = st.Page(
    page="CosmoBot.py",
    title="CosmoBot",
    icon=":material/dashboard:",
    default=True,
)

Project_side_page_1 = st.Page(
    page="Info_page.py",
    title="Info",
    icon=":material/info:",
)


# Navigation setup
pg = st.navigation(pages=[CosmoBotpage, Project_side_page_1])

# Handle page navigation using session state
if 'current_page' not in st.session_state:
    st.session_state['current_page'] = 'CosmoBot.py'

# Set the page based on session state
pg.run()
