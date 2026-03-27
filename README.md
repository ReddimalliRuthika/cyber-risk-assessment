# 🛡️ Cyber Risk Assessment & Threat Intelligence Platform

## 📌 Project Overview

The **Cyber Risk Assessment System** is a Python-based platform designed to automate vulnerability scanning, risk analysis, and threat intelligence integration.

It helps organizations identify security risks, analyze threats, and generate actionable reports to improve their cybersecurity posture.

---

## 🚀 Features

* 🔍 **Port Scanning**

  * Detects open ports and running services using Nmap

* 🌐 **Threat Intelligence Integration**

  * Uses VirusTotal API for real-time threat analysis

* 📊 **Risk Scoring System**

  * Calculates exposure, threat score, and overall risk

* 📈 **Interactive Dashboard**

  * Built with Streamlit for real-time visualization

* 📜 **Scan History**

  * Stores previous scans using SQLite database

* 📄 **Report Generation**

  * Download reports in PDF, CSV, and JSON formats

* 📧 **Email Alerts**

  * Sends alerts for high and critical risks

* 🔗 **REST API**

  * FastAPI-based endpoints for accessing scan data

---

## 🏗️ Project Structure

```
cyber-risk-assessment/
│
├── dashboard/
│   ├── home.py
│   └── pages/
│       ├── 1_app.py
│       ├── 2_analysis.py
│       ├── 3_scan_data.py
│       ├── 4_history.py
│       └── 5_download_report.py
│
├── modules/
│   ├── analyser.py
│   ├── database.py
│   ├── emailer.py
│   ├── report.py
│   └── scanner.py
│
├── api.py
├── ui.py
├── requirements.txt
├── README.md
├── license.txt
└── .gitignore
```

---

## ⚙️ Technologies Used

* **Frontend:** Streamlit

* **Backend:** Python

* **API:** FastAPI

* **Database:** SQLite

* **Libraries:**

  * pandas
  * plotly
  * requests
  * python-dotenv
  * fpdf

* **Tools & APIs:**

  * Nmap (Port Scanning)
  * VirusTotal API (Threat Intelligence)

---

## 🛠️ Installation & Setup

### 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Setup Environment Variables

Create a `.env` file in the root directory:

```
VT_API_KEY=your_virustotal_api_key
EMAIL_SENDER=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
```

---

## ▶️ Running the Project

### 🔹 Run Streamlit Dashboard

```bash
streamlit run dashboard/home.py
```

### 🔹 Run FastAPI Server

```bash
uvicorn api:app --reload
```

---

## 📊 API Endpoints

| Endpoint                    | Description          |
| --------------------------- | -------------------- |
| `/`                         | Check API status     |
| `/results`                  | Get all scan results |
| `/results/severity/{level}` | Filter by severity   |
| `/results/ip/{ip}`          | Filter by IP         |

---

## 📈 Risk Calculation

Risk score is calculated using:

* Exposure Score (based on service)
* Threat Score (VirusTotal data)

```
Risk Score = (Exposure × 0.6) + (Threat × 0.4)
```

Severity Levels:

* 🔥 Critical
* ⚠️ High
* 🟡 Medium
* 🟢 Low

---

## 📄 Output

* 📊 Dashboard Visualizations
* 📜 Scan History
* 📄 PDF Reports
* 📧 Email Alerts

---

## 🔒 Security Features

* Real-time vulnerability detection
* Threat intelligence integration
* Risk-based prioritization
* Alert notifications

---

## 🚀 Future Enhancements

* 🔐 User Authentication (JWT/OAuth)
* ☁️ Cloud Deployment
* 📡 Integration with Shodan/Nessus
* 📊 Advanced AI-based threat prediction
* 👥 Multi-user support

---

## 👩‍💻 Author

**Reddimalli Ruthika**

---

## 📜 License

This project is licensed under the MIT License.

---

