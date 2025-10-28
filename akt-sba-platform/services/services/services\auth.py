from __future__ import annotations
import streamlit as st
from services.supabase_client import get_supabase
from services.audit import audit

def _load_profile_into_state(user_id: str) -> None:
    sb = get_supabase()
    resp = sb.table("app_users").select("*").eq("id", user_id).single().execute()
    profile = resp.data if hasattr(resp, "data") else None
    st.session_state["auth_user"] = profile
    st.session_state["role"] = (profile or {}).get("role", "anonymous")
    st.session_state["status"] = (profile or {}).get("status", "pending")

def sign_in(email: str, password: str) -> tuple[bool, str]:
    sb = get_supabase()
    try:
        auth_resp = sb.auth.sign_in_with_password({"email": email, "password": password})
        user = auth_resp.user
        if not user:
            return False, "Invalid credentials."
        _ensure_profile_exists(user.id, email, eager=False)
        _load_profile_into_state(user.id)
        audit("auth.sign_in", {"email": email})
        return True, "Signed in."
    except Exception as e:
        return False, f"Sign-in failed: {e}"

def sign_up(email: str, display_name: str, password: str) -> tuple[bool, str]:
    sb = get_supabase()
    try:
        res = sb.auth.sign_up({"email": email, "password": password})
        user = res.user
        if not user:
            return False, "Sign-up failed."
        _ensure_profile_exists(user.id, email, display_name=display_name, eager=True)
        _load_profile_into_state(user.id)
        audit("auth.sign_up", {"email": email})
        return True, "Account created. Status is 'pending' until an admin approves."
    except Exception as e:
        return False, f"Sign-up failed: {e}"

def sign_out() -> None:
    sb = get_supabase()
    try:
        sb.auth.sign_out()
    except Exception:
        pass
    st.session_state.clear()
    audit("auth.sign_out", {})

def _ensure_profile_exists(user_id: str, email: str, display_name: str | None = None, eager: bool = False) -> None:
    """Insert profile row if missing (defaults: role=user, status=pending)."""
    sb = get_supabase()
    got = sb.table("app_users").select("id").eq("id", user_id).maybe_single().execute()
    exists = bool(getattr(got, "data", None))
    if not exists:
        payload = {
            "id": user_id,
            "email": email,
            "display_name": display_name or email.split("@")[0],
            "role": "user",
            "status": "pending"
        }
        sb.table("app_users").insert(payload).execute()

def needs_admin_bootstrap() -> bool:
    """True if no primary_admin exists yet."""
    sb = get_supabase()
    resp = sb.table("app_users").select("id").eq("role", "primary_admin").limit(1).execute()
    data = getattr(resp, "data", None) or []
    return len(data) == 0

def try_bootstrap_current_user_as_primary_admin(code: str) -> tuple[bool, str]:
    """If no primary_admin exists and code matches secrets, promote current user."""
    if not st.session_state.get("auth_user"):
        return False, "You must sign in first."
    if not needs_admin_bootstrap():
        return False, "A Primary Admin already exists."

    expected = st.secrets.get("PRIMARY_ADMIN_BOOTSTRAP_CODE", "")
    if not expected or code.strip() != str(expected).strip():
        return False, "Invalid bootstrap code."

    sb = get_supabase()
    user_id = st.session_state["auth_user"]["id"]
    sb.table("app_users").update({"role": "primary_admin", "status": "active"}).eq("id", user_id).execute()
    _load_profile_into_state(user_id)
    audit("admin.bootstrap_primary", {"user_id": user_id})
    return True, "You are now the Primary Admin."
