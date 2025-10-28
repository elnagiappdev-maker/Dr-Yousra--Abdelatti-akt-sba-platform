import os, streamlit as st
from app.constants import APP_TITLE, BRAND_LINE, ASSETS_WALLPAPER_CANDIDATES, PLACEHOLDER_WALLPAPER_CSS, DEFAULT_PAGE_DESC
def _find_wallpaper_path():
    for p in ASSETS_WALLPAPER_CANDIDATES:
        if os.path.exists(p):
            return p
    return None
def apply_base_page_setup():
    st.set_page_config(page_title=APP_TITLE, page_icon="🩺", layout="wide", initial_sidebar_state="expanded")
    st.markdown(f"<style>{PLACEHOLDER_WALLPAPER_CSS}</style>", unsafe_allow_html=True)
    st.title(APP_TITLE); st.caption(DEFAULT_PAGE_DESC)
def render_wallpaper_banner():
    image_path = _find_wallpaper_path()
    if image_path:
        st.image(image_path, use_container_width=True, caption="Wallpaper banner")
    else:
        st.markdown('<div class="banner-placeholder">Wallpaper not found (assets/brand/yousra.jpg or yousra.png). Use the uploader below to add it.</div>', unsafe_allow_html=True)
        with st.expander("Upload wallpaper (yousra.jpg/.png)"):
            file = st.file_uploader("Select portrait", type=["jpg","jpeg","png"], key="wallpaper_uploader")
            if file is not None:
                st.session_state["uploaded_wallpaper"] = file.read()
                st.success("Wallpaper uploaded for this session.")
    st.markdown(f'<div class="watermark no-select">{BRAND_LINE}</div>', unsafe_allow_html=True)
def render_footer():
    st.markdown(f'<div class="footer-legal no-select">{BRAND_LINE}</div>', unsafe_allow_html=True)
