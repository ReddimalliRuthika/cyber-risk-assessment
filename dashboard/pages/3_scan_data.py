import sys, os, json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# ✅ Import UI
from ui import apply_ui
apply_ui()


import streamlit as st

# 📂 Page title
st.title("📂 Scan Data")

# ⚠️ Check if scan data exists in session
if "scan_df" not in st.session_state:
    st.warning("⚠️ Run a scan first")

else:
    # 📊 Display the scanned data in table format
    st.dataframe(st.session_state["scan_df"])