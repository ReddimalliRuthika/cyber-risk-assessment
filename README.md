# 🛡️ Cyber Risk Assessment & Threat Intelligence Platform

## 📌 Project Overview

The **Cyber Risk Assessment System** is a Python-based platform designed to automate vulnerability scanning, analyze risks, and provide actionable threat intelligence.

It helps organizations detect security weaknesses, evaluate risk levels, and improve their cybersecurity posture. The system integrates tools like **Nmap** for scanning and **VirusTotal API** for threat intelligence, with results visualized through an interactive **Streamlit dashboard**.

---

## 🎯 Objectives

* Automate vulnerability scanning (ports & services)
* Integrate threat intelligence (VirusTotal API)
* Calculate risk scores based on exposure & threats
* Provide real-time dashboards and analytics
* Send alerts for high/critical risks
* Generate downloadable reports (PDF, CSV, JSON)

---

## 🏗️ System Architecture

### 🔹 Components:

1. **Frontend Dashboard**

   * Built using Streamlit
   * Displays scan results, analytics, and reports

2. **Scanning Engine**

   * Uses Nmap for port/service detection

3. **Threat Intelligence Layer**

   * Integrates VirusTotal API

4. **Analytics Engine**

   * Computes risk scores and severity levels

5. **Database Layer**

   * Uses SQLite to store scan history

6. **API Layer**

   * Built with FastAPI

7. **Notification System**

   * Sends email alerts using SMTP

---

## ⚙️ Technology Stack

| Technology         | What it Does in This Project                                                                            |
| ------------------ | ------------------------------------------------------------------------------------------------------- |
| **Python**         | Main programming language used to build backend logic, integrate modules, and control the entire system |
| **Streamlit**      | Creates an interactive web dashboard where users input targets and view scan results                    |
| **Plotly**         | Used for visualizing data through charts like bar graphs, pie charts, heatmaps, and trends              |
| **Nmap**           | Performs network scanning to detect open ports and running services on target systems                   |
| **VirusTotal API** | Provides threat intelligence by checking whether an IP address is malicious or suspicious               |
| **SQLite**         | Stores scan results and history in a lightweight local database                                         |
| **FastAPI**        | Builds REST APIs to access scan data programmatically                                                   |
| **FPDF**           | Generates PDF reports containing scan results and risk summaries                                        |
| **SMTP (Email)**   | Sends alert emails to users when high or critical risks are detected                                    |
| **python-dotenv**  | Loads sensitive data like API keys and email credentials securely from `.env` file                      |

---

## 🧩 Modules Description

### 🔍 1. Vulnerability Scanning Engine (`scanner.py`)

* Runs Nmap scans on targets
* Extracts:

  * IP address
  * Open ports
  * Running services

---

### 🌐 2. Threat Intelligence Module

* Uses VirusTotal API
* Retrieves:

  * Malicious count
  * Suspicious count

---

### 📊 3. Risk Scoring & Analytics (`analyser.py`)

#### Risk Calculation:

* **Exposure Score:**

  * High-risk (FTP, Telnet, RDP) → 8
  * Medium (HTTP, SSH) → 5
  * Low → 2

* **Threat Score:**

```
Threat Score = (Malicious × 2) + Suspicious
```

* **Final Risk Score:**

```
Risk Score = (Exposure × 0.6) + (Threat × 0.4)
```

#### Severity Levels:

| Score | Severity    |
| ----- | ----------- |
| ≥ 7   | 🔥 Critical |
| ≥ 5   | ⚠️ High     |
| ≥ 3   | 🟡 Medium   |
| < 3   | 🟢 Low      |

---

### 📈 4. Dashboard & Visualization

* Service distribution (Bar chart)
* Severity breakdown (Pie chart)
* Risk heatmap (Scatter plot)
* Risk trends (Line graph)
* Risk hierarchy (Sunburst chart)

---

### 🗄️ 5. Database Module (`database.py`)

* Stores scan results in SQLite
* Maintains scan history
* Enables data retrieval

---

### 📧 6. Email Alert System (`emailer.py`)

* Sends alerts for:

  * High risks
  * Critical risks
* Includes:

  * Cause of vulnerability
  * Recommended actions

---

### 📄 7. Report Generation (`report.py`)

* Generates PDF reports
* Includes:

  * Summary
  * Risk details
  * Vulnerable services

---

### 🔗 8. API Module (`api.py`)

| Endpoint                    | Description        |
| --------------------------- | ------------------ |
| `/results`                  | Get all scan data  |
| `/results/severity/{level}` | Filter by severity |
| `/results/ip/{ip}`          | Filter by IP       |

---

## 🖥️ User Interface

### 🏠 Home Page

* Overview of features
* Launch dashboard

### 📊 Dashboard Page

* Input:

  * Target IP/domain
  * Email
* Output:

  * Scan results
  * Risk summary
  * Filters

### 📈 Analysis Page

* Heatmaps
* Trends
* Service analysis

### 📜 History Page

* View previous scans

### 📄 Reports Page

* Download:

  * PDF
  * CSV
  * JSON

---

## 🔄 Workflow

1. User enters targets
2. System runs Nmap scan
3. Extracts open ports & services
4. Calls VirusTotal API
5. Calculates risk score
6. Stores data in database
7. Displays results in dashboard
8. Sends alert email (if needed)
9. Generates reports

---

## 🔒 Security Features

* API key protection using `.env`
* Secure email authentication (SMTP SSL)
* Input validation for targets and email
* No sensitive data exposed in UI

---

## 📊 Outputs

* 📊 Risk dashboards
* 📧 Email alerts
* 📄 PDF reports
* 📁 CSV/JSON exports
* 📜 Scan history logs

---

## ✅ Advantages

* Fully automated scanning
* Real-time threat intelligence
* Easy-to-use dashboard
* Lightweight and fast
* Scalable architecture

---

## ⚠️ Limitations

* Depends on external APIs (VirusTotal)
* Requires Nmap installation
* Basic risk scoring (not full CVSS)
* Limited deep vulnerability scanning

---

## 🚀 Future Enhancements

* AI-based anomaly detection
* Cloud deployment
* Real-time monitoring system

---

## 🛠️ How to Run the Project

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Setup Environment Variables

Create a `.env` file:

```
VT_API_KEY=your_api_key
EMAIL_SENDER=your_email
EMAIL_PASSWORD=your_password
```

### Step 3: Run Streamlit App

```bash
streamlit run dashboard/home.py
```

### Step 4: Run API (Optional)

```bash
uvicorn api:app --reload
```

---

## 👩‍💻 Author

**Reddimalli Ruthika**

---

## 📜 License

This project is licensed under the MIT License.

---

## 🧾 Conclusion

This project successfully implements a **Cyber Risk Assessment Platform** that automates scanning, analyzes vulnerabilities, and provides actionable insights.

It enables organizations to proactively identify risks, improve security posture, and ensure better compliance with cybersecurity standards.

---
