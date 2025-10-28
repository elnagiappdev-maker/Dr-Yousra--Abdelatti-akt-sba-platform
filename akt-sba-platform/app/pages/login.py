import streamlit as st

def render() -> None:
    st.subheader("Login / Sign Up (placeholder)")
    st.info(
        "Email/Password authentication and admin approval workflow will be implemented in **Step 1** using Supabase. "
        "For now, this is a visual placeholder."
    )

    tab_login, tab_signup = st.tabs(["Sign In", "Sign Up"])
    with tab_login:
        st.text_input("Email", key="login_email", placeholder="you@example.com")
        st.text_input("Password", type="password", key="login_password")
        st.button("Sign In (disabled)", disabled=True)

    with tab_signup:
        st.text_input("Email", key="signup_email", placeholder="you@example.com")
        st.text_input("Display name", key="signup_display_name", placeholder="Your name")
        st.text_input("Password", type="password", key="signup_password")
        st.text_input("Confirm password", type="password", key="signup_confirm_password")
        st.button("Create Account (disabled)", disabled=True)

    st.caption("Admin approval required before full access. (Coming in Step 1–2.)")
