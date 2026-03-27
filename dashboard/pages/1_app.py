import streamlit as st
import pandas as pd
import sys, os, time
from dotenv import load_dotenv

# ✅ MUST BE FIRST
st.set_page_config(page_title="Cyber Risk Dashboard", layout="wide")


# 🔐 LOAD ENV VARIABLES
load_dotenv()
VT_API_KEY = os.getenv("VT_API_KEY")

# 📁 FIX PATH FOR MODULE IMPORTS
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# ✅ APPLY GLOBAL UI
from ui import apply_ui
apply_ui()

# 🔗 Import project modules
from modules.scanner import run_nmap_scan, parse_nmap_xml, check_virustotal
from modules.analyser import enrich_dataframe
from modules.database import save_scan
from modules.emailer import send_alert_email


# ─────────────────────────────
# 🎨 PAGE-SPECIFIC CSS
# ─────────────────────────────
st.markdown("""
<style>
.big-title {
    font-size: 36px;
    font-weight: 700;
}

.input-label {
    font-size: 22px;
    font-weight: 600;
    margin-bottom: 6px;
}

.glass {
    background: rgba(255,255,255,0.05);
    padding: 15px;
    border-radius: 12px;
    border: 1px solid rgba(255,255,255,0.1);
    margin-bottom: 10px;
}

.stButton > button {
    height: 50px;
    font-size: 16px;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────
# 🧭 HEADER
# ─────────────────────────────
st.markdown('<div class="big-title">🛡️ Cyber Risk Assessment Dashboard</div>', unsafe_allow_html=True)
st.caption("🚀 Real-time Vulnerability Scanner")

st.divider()


# ─────────────────────────────
# 🎯 INPUT SECTION
# ─────────────────────────────
st.markdown('<div class="input-label">🎯 Enter Targets (comma separated)</div>', unsafe_allow_html=True)

targets_input = st.text_input(
    "",
    placeholder="scanme.nmap.org, testphp.vulnweb.com"
)

st.markdown('<div class="input-label">📧 Enter your Email for Alerts</div>', unsafe_allow_html=True)

user_email = st.text_input(
    "",
    placeholder="example@gmail.com"
)


# 🔘 BUTTONS
col1, col2 = st.columns(2)
run = col1.button("🚀 Run Scan", use_container_width=True)
refresh = col2.button("🔄 Refresh", use_container_width=True)

if refresh:
    st.session_state.clear()
    st.rerun()


# ─────────────────────────────
# 🔍 SCAN PROCESS
# ─────────────────────────────
if run:

    if not targets_input:
        st.warning("⚠️ Please enter at least one target")
        st.stop()

    if not user_email:
        st.warning("⚠️ Please enter your email")
        st.stop()

    if "@" not in user_email:
        st.warning("⚠️ Enter a valid email")
        st.stop()

    targets = [t.strip() for t in targets_input.split(",") if t.strip()]
    total = len(targets)

    title_box = st.empty()
    progress_bar = st.progress(0)
    status_box = st.empty()
    log_box = st.empty()

    title_box.markdown("### 🔍 Scan in Progress...")

    all_data = []

    for i, target in enumerate(targets):

        status_box.markdown(f"""
        <div class="glass">
        🔎 <b>Scanning Target {i+1}/{total}</b><br>
        🌐 {target}
        </div>
        """, unsafe_allow_html=True)

        with st.spinner(f"Scanning {target}..."):
            xml = run_nmap_scan(target)
            rows = parse_nmap_xml(xml)
            time.sleep(0.5)

        for r in rows:
            r["target"] = target

        with log_box.container():
            if rows:
                st.success(f"✅ {target} → {len(rows)} open ports")
            else:
                st.warning(f"⚠️ {target} → No open ports")

        all_data.extend(rows)
        progress_bar.progress((i + 1) / total)

    title_box.empty()
    status_box.empty()
    progress_bar.empty()
    log_box.empty()

    if not all_data:
        st.error("❌ No scan data collected")
        st.stop()

    df = pd.DataFrame(all_data)

    # 🌐 VirusTotal
    with st.spinner("🌐 Fetching Threat Intelligence..."):
        vt_data = {}
        for ip in df["ip"].unique():
            vt_data[ip] = check_virustotal(ip, VT_API_KEY)

    df = enrich_dataframe(df, vt_data)
    df["scan_time"] = pd.Timestamp.now()

    save_scan(df)

    email_status = send_alert_email(df, user_email)

    if email_status == "sent":
        st.success("📧 Alert email sent successfully!")
    elif email_status == "no_risk":
        st.info("ℹ️ No high/critical risks detected")
    elif email_status == "no_email":
        st.warning("⚠️ Enter email to receive alerts")
    else:
        st.error("❌ Failed to send email")

    st.session_state["scan_df"] = df
    st.success("🎉 Scan Completed Successfully!")


# ─────────────────────────────
# 📊 RESULTS DISPLAY
# ─────────────────────────────
if "scan_df" in st.session_state:

    df = st.session_state["scan_df"]

    st.divider()
    st.subheader("📊 Summary")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("🖥️ Hosts", df["ip"].nunique())
    col2.metric("🔓 Ports", len(df))
    col3.metric("⚠️ High", (df["severity"] == "High").sum())
    col4.metric("🔥 Critical", (df["severity"] == "Critical").sum())

    col5, col6, col7 = st.columns(3)

    col5.metric("📈 Avg Risk", round(df["risk_score"].mean(), 2))
    col6.metric("⚡ Most Risky Service", df.groupby("service")["risk_score"].mean().idxmax())
    col7.metric("🎯 Most Vulnerable Host", df.groupby("ip")["risk_score"].sum().idxmax())

    st.divider()

    st.subheader("🔍 Filters")

    colf1, colf2, colf3 = st.columns(3)

    severity_filter = colf1.selectbox("Severity", ["All"] + sorted(df["severity"].unique()))
    ip_filter = colf2.selectbox("IP", ["All"] + sorted(df["ip"].unique()))
    service_filter = colf3.selectbox("Service", ["All"] + sorted(df["service"].unique()))

    filtered_df = df.copy()

    if severity_filter != "All":
        filtered_df = filtered_df[filtered_df["severity"] == severity_filter]

    if ip_filter != "All":
        filtered_df = filtered_df[filtered_df["ip"] == ip_filter]

    if service_filter != "All":
        filtered_df = filtered_df[filtered_df["service"] == service_filter]

    st.divider()

    st.subheader("🔥 Top 5 Risky Hosts")

    top_risk = (
        df.groupby("ip")["risk_score"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
        .reset_index()
    )

    st.dataframe(top_risk, use_container_width=True)

    st.divider()

    st.subheader("📂 Scan Results")
    st.dataframe(filtered_df, use_container_width=True)

else:
    st.info("👉 Enter targets and click 'Run Scan'")