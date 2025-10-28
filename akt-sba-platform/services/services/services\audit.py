from __future__ import annotations
from typing import Any, Dict, Optional
import streamlit as st
from services.supabase_client import get_supabase

def audit(action: str, details: Optional[Dict[str, Any]] = None) -> None:
    """Best-effort audit insert. Non-fatal if it fails."""
    try:
        sb = get_supabase()
        user_id = None
        if "auth_user" in st.session_state and st.session_state["auth_user"]:
            user_id = st.session_state["auth_user"].get("id")
        payload = {
            "user_id": user_id,
            "action": action,
            "details": details or {},
        }
        sb.table("audit").insert(payload).execute()
    except Exception:
        # Keep UI resilient
        pass
