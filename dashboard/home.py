import streamlit as st

# 🌐 Page config
st.set_page_config(page_title="Cyber Risk Dashboard", layout="wide")

# 🎨 Glassmorphism CSS
st.markdown("""
<style>

/* 🌌 Background */
.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    color: white;
}

/* 🏷️ Titles */
.main-title {
    font-size: 42px;
    font-weight: 700;
    text-align: center;
    color: white;
}
.subtitle {
    font-size: 18px;
    text-align: center;
    color: #cbd5f5;
}

/* 🧊 Glass Card (FIXED SIZE) */
.card {
    background: rgba(255, 255, 255, 0.08);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border-radius: 18px;
    border: 1px solid rgba(255,255,255,0.15);

    padding: 25px;

    /* 🔥 FIX: same size */
    height: 180px;

    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;

    text-align: center;
    transition: 0.3s;
}

/* ✨ Hover effect */
.card:hover {
    transform: translateY(-8px) scale(1.02);
    box-shadow: 0px 8px 30px rgba(0,0,0,0.4);
}

/* 🔘 Button */
.stButton > button {
    height: 55px;
    font-size: 18px;
    border-radius: 12px;
    background: linear-gradient(135deg, #2563eb, #1e40af);
    color: white;
    font-weight: bold;
    border: none;
}

/* ✨ Divider */
hr {
    border: 1px solid rgba(255,255,255,0.1);
}

/* 🔥 FIX: equal column height */
div[data-testid="column"] {
    display: flex;
}

</style>
""", unsafe_allow_html=True)

# 🏠 HEADER
st.markdown('<div class="main-title">🛡️ Cyber Risk Assessment System</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">🚀 Scan • Analyze • Protect your systems in real-time</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.divider()

# 📊 FEATURES
st.subheader("✨ Key Features")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <h3>🔍 Port Scanning</h3>
        <p>Detect open ports and running services using Nmap</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h3>⚠️ Threat Intelligence</h3>
        <p>Integrates VirusTotal for real-time threat analysis</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <h3>📊 Risk Analysis</h3>
        <p>Calculates risk score and severity levels</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 📂 MORE FEATURES
col4, col5, col6 = st.columns(3)

with col4:
    st.markdown("""
    <div class="card">
        <h3>📜 Scan History</h3>
        <p>Stores and displays previous scans from database</p>
    </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown("""
    <div class="card">
        <h3>📄 Reports</h3>
        <p>Download results as PDF, CSV, and JSON</p>
    </div>
    """, unsafe_allow_html=True)

with col6:
    st.markdown("""
    <div class="card">
        <h3>📧 Email Alerts</h3>
        <p>Receive alerts for high and critical risks</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# 🚀 CALL TO ACTION
st.subheader("🚀 Start Your Scan")

st.markdown("Click below to launch the dashboard and begin scanning your targets.")

if st.button("🚀 Launch Dashboard", use_container_width=True):
    st.switch_page("pages/1_app.py")