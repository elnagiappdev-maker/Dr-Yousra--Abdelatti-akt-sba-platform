import streamlit as st
from app.pages.home import render as render_home
from app.pages.login import render as render_login
from app.pages.dashboard import render as render_dashboard
from app.pages.admin import render as render_admin
def _block_if_pending_or_blocked():
    status = st.session_state.get("status", "pending")
    if status == "pending":
        st.warning("Your account is **pending approval**. An admin must activate your access."); return True
    if status == "blocked":
        st.error("Your account is blocked. Contact the administrator."); return True
    return False
def route(page_name: str):
    if page_name == "Home": return render_home()
    if page_name == "Login": return render_login()
    if not st.session_state.get("auth_user"):
        st.info("Please sign in to access this page."); return render_login()
    if _block_if_pending_or_blocked(): return
    if page_name == "Dashboard": return render_dashboard()
    if page_name == "Admin": return render_admin()
    st.error("Page not found.")
