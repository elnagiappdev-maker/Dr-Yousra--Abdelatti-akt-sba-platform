import streamlit as st
from services.auth import sign_in, sign_up, sign_out, needs_admin_bootstrap, try_bootstrap_current_user_as_primary_admin

def render() -> None:
    st.subheader("Login / Sign Up")

    # Sign-out button if logged in
    if st.session_state.get("auth_user"):
        st.success(f"Signed in as: {st.session_state['auth_user'].get('email')}")
        col1, col2 = st.columns([1,1])
        with col1:
            if st.button("Sign out"):
                sign_out()
                st.rerun()
        with col2:
            st.write(f"Role: **{st.session_state.get('role')}** | Status: **{st.session_state.get('status')}**")
    else:
        tab_login, tab_signup = st.tabs(["Sign In", "Sign Up"])

        with tab_login:
            email = st.text_input("Email", key="login_email", placeholder="you@example.com")
            pwd = st.text_input("Password", type="password", key="login_password")
            if st.button("Sign In"):
                ok, msg = sign_in(email, pwd)
                if ok:
                    st.success(msg)
                    st.rerun()
                else:
                    st.error(msg)

        with tab_signup:
            email2 = st.text_input("Email", key="signup_email", placeholder="you@example.com")
            name2 = st.text_input("Display name", key="signup_display_name", placeholder="Your name")
            pwd2 = st.text_input("Password", type="password", key="signup_password")
            pwdc = st.text_input("Confirm password", type="password", key="signup_confirm_password")
            if st.button("Create Account"):
                if not email2 or not pwd2:
                    st.error("Email and password are required.")
                elif pwd2 != pwdc:
                    st.error("Passwords do not match.")
                else:
                    ok, msg = sign_up(email2, name2 or email2.split("@")[0], pwd2)
                    if ok:
                        st.success(msg)
                        st.info("Please sign in now. Your status is **pending** until an admin activates you.")
                    else:
                        st.error(msg)

    # Admin bootstrap (only appears if no primary admin exists)
    if needs_admin_bootstrap():
        st.info("No **Primary Admin** exists yet. The first user can bootstrap with the one-time code.")
        code = st.text_input("Enter PRIMARY_ADMIN_BOOTSTRAP_CODE")
        if st.button("Bootstrap me as Primary Admin"):
            ok, msg = try_bootstrap_current_user_as_primary_admin(code.strip())
            if ok:
                st.success(msg)
                st.rerun()
            else:
                st.error(msg)
