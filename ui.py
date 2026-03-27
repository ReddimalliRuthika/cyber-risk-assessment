import streamlit as st

def apply_ui():
    st.markdown("""
    <style>

    /* 🌌 BACKGROUND (Dark + Light Support) */
    html[data-theme="dark"] .stApp {
        background: linear-gradient(135deg, #0f172a, #1e293b);
        color: white;
    }

    html[data-theme="light"] .stApp {
        background: linear-gradient(135deg, #f8fafc, #e2e8f0);
        color: #111827;
    }

    /* 🏷️ TITLES */
    .main-title {
        font-size: 42px;
        font-weight: 700;
        text-align: center;
    }

    .subtitle {
        font-size: 18px;
        text-align: center;
        opacity: 0.8;
    }

    /* 🧊 GLASS CARD */
    .card {
        min-height: 150px;
        display: flex;
        flex-direction: column;
        justify-content: center;

        background: rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);

        border-radius: 18px;
        border: 1px solid rgba(255,255,255,0.15);
        padding: 25px;
        text-align: center;
        transition: 0.3s;
    }

    /* ✨ Hover */
    .card:hover {
        transform: translateY(-8px) scale(1.02);
        box-shadow: 0px 8px 30px rgba(0,0,0,0.4);
    }

    /* 🔘 BUTTON STYLE */
    .stButton > button {
        height: 55px;
        font-size: 18px;
        border-radius: 12px;
        background: linear-gradient(135deg, #2563eb, #1e40af);
        color: white;
        font-weight: bold;
        border: none;
        transition: 0.3s;
    }

    .stButton > button:hover {
        transform: scale(1.03);
        box-shadow: 0px 6px 20px rgba(37,99,235,0.4);
    }

    /* ✨ DIVIDER */
    hr {
        border: 1px solid rgba(255,255,255,0.1);
    }

    /* =========================
       🔥 INPUT FIX (IMPORTANT)
       ========================= */

    /* 🌙 DARK MODE INPUT */
    html[data-theme="dark"] input {
        background-color: rgba(255,255,255,0.08) !important;
        color: white !important;
        border: 1px solid rgba(255,255,255,0.2) !important;
        border-radius: 12px !important;
        padding: 10px !important;
    }

    /* ☀️ LIGHT MODE INPUT */
    html[data-theme="light"] input {
        background-color: rgba(255,255,255,0.95) !important;
        color: #111827 !important;
        border: 1px solid rgba(0,0,0,0.1) !important;
        border-radius: 12px !important;
        padding: 10px !important;
    }

    /* ✍️ PLACEHOLDER */
    html[data-theme="dark"] input::placeholder {
        color: rgba(255,255,255,0.5);
    }

    html[data-theme="light"] input::placeholder {
        color: rgba(0,0,0,0.4);
    }

    /* 📦 SUCCESS / ALERT BOX IMPROVEMENT */
    html[data-theme="dark"] .stAlert {
        border-radius: 12px;
        background: rgba(34,197,94,0.15);
        border: 1px solid rgba(34,197,94,0.3);
    }

    html[data-theme="light"] .stAlert {
        border-radius: 12px;
    }

    </style>
    """, unsafe_allow_html=True)