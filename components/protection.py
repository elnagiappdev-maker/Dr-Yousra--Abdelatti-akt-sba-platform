import streamlit as st
MINIMAL_JS = r"""
<script>
  document.addEventListener('contextmenu', event => event.preventDefault());
  document.addEventListener('keydown', function(e) {
    if ((e.ctrlKey || e.metaKey) && (e.key === 'c' || e.key === 'p')) { e.preventDefault(); }
    if (e.key === 'PrintScreen') { e.preventDefault(); alert('Screenshots are restricted. This attempt may be logged.'); }
  });
</script>
"""
def inject_minimal_protection():
    st.markdown(MINIMAL_JS, unsafe_allow_html=True)
