import streamlit as st

def render() -> None:
    st.subheader("Home")
    st.markdown(
        """
        Welcome to the **MRCGP(UK) AKT SBA** training platform.
        
        **What’s here now (Step 0):**
        - Clean Streamlit scaffold with navigation and global branding/footer
        - Wallpaper banner with upload placeholder
        - Minimal content-protection hooks (context menu disabled; selection disabled)
        
        **What’s coming next:**
        - Step 1: Supabase Auth + Database schema; email/password sign-up; admin approval gate
        - Step 2: RBAC & Admin Console with approvals and audit log
        - Step 3: Item authoring with strict RCGP AKT SBA linter & references manager
        - Step 4–6: Delivery engine, analytics, and stronger content-protection
        - Step 7: Sample AKT-level items
        - Step 8: Accessibility, tests, and hardening
        """
    )
