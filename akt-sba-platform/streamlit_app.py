import streamlit as st
from app.router import route
from app.layout import render_wallpaper_banner, render_footer, apply_base_page_setup
from services.state import init_session_state
from components.protection import inject_minimal_protection

# ---------- Base page setup ----------
apply_base_page_setup()
inject_minimal_protection()  # Light, non-invasive protections (context-menu off, no-select)
init_session_state()

# ---------- Sidebar navigation ----------
st.sidebar.title("AKT SBA Platform")
page = st.sidebar.radio(
    "Navigation",
    options=["Home", "Login", "Dashboard", "Admin"],
    index=0,
    help="Use this menu to navigate between pages."
)
st.sidebar.divider()
st.sidebar.caption("High-contrast mode and other toggles will arrive in Step 8.")

# ---------- Wallpaper banner (gracefully handles missing yousra image) ----------
render_wallpaper_banner()

# ---------- Route to page ----------
route(page)

# ---------- Global footer (branding/legal) ----------
render_footer()
