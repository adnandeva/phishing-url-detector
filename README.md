# 🔐 Phishing URL Detection using Machine Learning

## Overview

This project detects whether a URL is legitimate or phishing using Machine Learning.

The system analyzes lexical and structural URL features such as:
- URL length
- Special characters
- Number of dots/subdomains
- Digits
- Hyphen usage
- IP-based URLs
- HTTPS usage
- Suspicious phishing keywords

The project uses a Random Forest classifier trained on a balanced real-world phishing dataset and includes an interactive Streamlit web application for real-time predictions.

---

## 🚀 Live Demo

👉 https://phishing-detector-adnan.streamlit.app

---

## ✨ Features

- Machine Learning based phishing detection
- Real-time URL analysis
- Random Forest classification
- URL normalization support
- Trusted domain whitelist
- IP address detection
- Suspicious keyword detection
- Confidence score visualization
- Explainable phishing indicators
- Streamlit web interface

---

## 🧠 Models Used

| Model | Purpose |
|---|---|
| Logistic Regression | Baseline comparison |
| Decision Tree | Rule-based classification |
| Random Forest | Final deployed model |

---

## 📊 Final Model Performance

### Random Forest Accuracy

| Metric | Score |
|---|---|
| Accuracy | 99.85% |
| Precision | 1.00 |
| Recall | 1.00 |
| F1 Score | 1.00 |

---

### 📈 Feature Importance

| Feature | Importance |
|---|---|
| Number of Special Characters | 0.3644 |
| Number of Dots | 0.2577 |
| Number of Digits | 0.1477 |
| URL Length | 0.0959 |
| Number of Subdomains | 0.0866 |
| HTTPS Usage | 0.0322 |
| IP Address Detection | 0.0109 |
| Hyphen Detection | 0.0047 |

The model primarily relies on structural URL complexity to identify phishing patterns.

---

## ⚙️ Key Improvements

### Dataset Upgrade
- Replaced the old dataset with a cleaner balanced real-world phishing dataset
- Reduced false positives on legitimate domains

### Improved Feature Engineering
Added:
- IP address detection
- Hyphen detection
- Subdomain analysis
- HTTPS detection
- Suspicious keyword detection

### Trusted Domain Whitelist
Integrated whitelist support for trusted domains such as:
- Google
- Microsoft
- GitHub
- Apple
- Amazon
- NASA

This prevents legitimate domains from being falsely classified as phishing.

### Enhanced Streamlit UI
Added:
- Confidence score visualization
- Suspicious indicator explanations
- Cleaner prediction feedback
- URL normalization support

---

## 🛠 Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Joblib

---

## 📂 Dataset

Dataset used:
- `phishing_url_dataset_unique.csv`

Contains:
- Legitimate URLs
- Real phishing URLs
- Balanced binary labels

---

## ▶️ How to Run Locally

### 1. Clone Repository

```bash
git clone https://github.com/adnandeva/phishing-url-detector.git
cd phishing-url-detector
```

### 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Train Model

```bash
python3 main.py
```

This generates:
```bash
model.pkl
```

### 5. Run Streamlit App

```bash
streamlit run app.py
```

---

## 📂 Project Structure

```text
phishing-url-detector/
│── app.py
│── main.py
│── model.pkl
│── dataset/
│   └── phishing_url_dataset_unique.csv
│── requirements.txt
│── README.md
```

---

## 🧪 Example Test URLs

### Safe URLs
- https://google.com
- https://github.com
- https://support.microsoft.com

### Phishing-like URLs
- http://paypal-login-verification-secure.com
- https://google.com.secure-login.xyz
- http://192.168.1.5/login.php

---

## 📌 Future Improvements

- WHOIS/domain age analysis
- VirusTotal API integration
- Advanced ensemble models
- SHAP explainability
- UI/UX enhancements

---

## 👤 Author

Adnan Riyaz  
Pre-Final Year Computer Science Student  
Ramaiah University of Applied Sciences
