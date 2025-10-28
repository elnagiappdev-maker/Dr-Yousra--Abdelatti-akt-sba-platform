import streamlit as st
from supabase import create_client, Client
_supabase: Client | None = None
def get_supabase() -> Client:
    global _supabase
    if _supabase is None:
        url = st.secrets["SUPABASE_URL"]
        key = st.secrets["SUPABASE_ANON_KEY"]
        _supabase = create_client(url, key)
    return _supabase
