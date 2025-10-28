import streamlit as st
def init_session_state():
    defaults = {
        "auth_user": None,
        "role": "anonymous",
        "status": "pending",
        "feature_flags": {},
        "uploaded_wallpaper": None,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v
