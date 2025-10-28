import streamlit as st

def render() -> None:
    st.subheader("Admin Console (placeholder)")
    st.warning(
        "User approvals, role management, audit logs, and feature toggles will be implemented in **Step 2**."
    )
    st.write(
        "Planned panels:\n"
        "- Pending users (approve / block)\n"
        "- Promote/demote roles (Primary Admin, Secondary Admin, User)\n"
        "- Audit log (paginated)\n"
        "- Feature flags"
    )
