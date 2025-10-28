import streamlit as st

def init_session_state() -> None:
    defaults = {
        "auth_user": None,                # will become dict with user info
        "role": "anonymous",              # 'anonymous' | 'user' | 'secondary_admin' | 'primary_admin'
        "feature_flags": {},              # will be hydrated from DB (Step 2)
        "uploaded_wallpaper": None,       # transient upload before Supabase storage
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v
