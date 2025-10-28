import streamlit as st
from app.pages.home import render as render_home
from app.pages.login import render as render_login
from app.pages.dashboard import render as render_dashboard
from app.pages.admin import render as render_admin

def route(page_name: str) -> None:
    # Centralized minimal router; will expand with auth guards in Step 2
    if page_name == "Home":
        render_home()
    elif page_name == "Login":
        render_login()
    elif page_name == "Dashboard":
        render_dashboard()
    elif page_name == "Admin":
        render_admin()
    else:
        st.error("Page not found.")
