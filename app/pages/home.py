import streamlit as st
def render():
    st.subheader("Home")
    st.markdown("""
Welcome to the **MRCGP(UK) AKT SBA** training platform.
**What’s here now (Step 1):**
- Streamlit scaffold with navigation and global branding/footer
- Wallpaper banner with upload placeholder
- Minimal content-protection hooks
- **Supabase Auth** with sign-up/sign-in and pending→active gate (bootstrap for Primary Admin)
""")
