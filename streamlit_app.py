import os, sys
THIS_DIR = os.path.dirname(os.path.abspath(__file__))
if THIS_DIR not in sys.path:
    sys.path.insert(0, THIS_DIR)

import streamlit as st
from app.router import route
from app.layout import render_wallpaper_banner, render_footer, apply_base_page_setup
from services.state import init_session_state
from components.protection import inject_minimal_protection

apply_base_page_setup()
inject_minimal_protection()
init_session_state()

st.sidebar.title("AKT SBA Platform")
page = st.sidebar.radio("Navigation", options=["Home", "Login", "Dashboard", "Admin"], index=0)
st.sidebar.divider()
st.sidebar.caption("High-contrast mode arrives in Step 8.")

render_wallpaper_banner()
route(page)
render_footer()
