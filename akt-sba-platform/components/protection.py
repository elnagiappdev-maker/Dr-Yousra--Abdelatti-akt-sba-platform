import streamlit as st

# NOTE: This is an early, light-touch protection; we will extend significantly in Step 6.
MINIMAL_JS = r"""
<script>
  // Disable context menu
  document.addEventListener('contextmenu', event => event.preventDefault());

  // Disable text selection & copy/print hotkeys
  document.addEventListener('keydown', function(e) {
    if ((e.ctrlKey || e.metaKey) && (e.key === 'c' || e.key === 'p')) {
      e.preventDefault();
    }
    // Basic PrintScreen detector (best-effort; not reliable)
    if (e.key === 'PrintScreen') {
      e.preventDefault();
      alert('Screenshots are restricted. This attempt may be logged.');
    }
  });
</script>
"""

def inject_minimal_protection() -> None:
    st.markdown(MINIMAL_JS, unsafe_allow_html=True)
