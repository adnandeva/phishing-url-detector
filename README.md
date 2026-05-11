# 🔐 Phishing URL Detection using Machine Learning and Lexical Feature Analysis

## 📌 Overview

This project detects whether a URL is **legitimate** or **phishing** using Machine Learning.

The system analyzes **lexical and structural URL features** without accessing webpage content, making predictions lightweight, fast, and efficient for real-time detection.

The project includes a trained **Random Forest classifier** along with an interactive **Streamlit web application** for live phishing analysis.

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
- Interactive Streamlit web interface

---

## 🧠 Models Used

| Model | Purpose |
|---|---|
| Logistic Regression | Baseline comparison |
| Decision Tree | Rule-based classification |
| Random Forest | Final deployed model |

---

## 📊 Final Model Performance

### Random Forest (Final Model)

| Metric | Score |
|---|---|
| Accuracy | 99.85% |
| Precision | 99.7% |
| Recall | 99.8% |
| F1 Score | 99.7% |

The Random Forest model achieved the best overall performance and was selected for deployment in the Streamlit application.

---

## 📈 Feature Importance

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

The model primarily relies on **structural URL complexity** to identify phishing patterns.

---

## ⚙️ Key Improvements

### ✅ Dataset Upgrade

- Replaced the previous dataset with a cleaner balanced real-world phishing dataset
- Reduced false positives on legitimate domains
- Improved detection consistency for real-world URLs

### ✅ Improved Feature Engineering

Added advanced lexical features including:

- IP address detection
- Hyphen detection
- Subdomain analysis
- HTTPS detection
- Suspicious keyword detection

### ✅ Trusted Domain Whitelist

Integrated whitelist support for trusted domains such as:

- Google

- Microsoft

- GitHub

- Apple

- Amazon

- NASA

The detector also supports trusted educational and government TLDs including:

- `.edu`

- `.gov`

- `.gov.in`

- `.ac.in`

This significantly reduces false positives for legitimate university, educational, and government portals.

### ✅ Enhanced Streamlit UI

Added:

- Confidence score visualization
- Suspicious indicator explanations
- Cleaner prediction feedback
- URL normalization support
- Real-time phishing probability display
- Trusted TLD based validation

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

### Dataset Used

`phishing_url_dataset_unique.csv`

### Contains

- Legitimate URLs
- Real phishing URLs
- Balanced binary labels

---

## ▶️ How to Run Locally

### 1️⃣ Clone Repository

```bash
git clone https://github.com/adnandeva/phishing-url-detector.git
cd phishing-url-detector
```

### 2️⃣ Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Train Model

```bash
python3 main.py
```

This generates:

```bash
model.pkl
```

### 5️⃣ Run Streamlit App

```bash
streamlit run app.py
```

---

## 📂 Project Structure

```bash
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

### ✅ Safe URLs

```text
https://google.com
https://github.com
https://support.microsoft.com
https://www.apple.com
https://ruasportal.msruas.ac.in
```

### 🚨 Phishing-like URLs

```text
http://paypal-login-verification-secure.com
https://google.com.secure-login.xyz
http://192.168.1.5/login.php
```

---

## 📌 Future Improvements

- WHOIS / domain age analysis
- VirusTotal API integration
- Advanced ensemble models
- SHAP explainability
- Improved UI/UX
- Live blacklist integration
- DNS reputation analysis

---

## 👤 Author

### Adnan Riyaz

Pre-Final Year Computer Science Student  
Ramaiah University of Applied Sciences

---

## ⭐ Acknowledgment

This project was built for learning, experimentation, and improving practical understanding of:

- Cybersecurity
- Phishing detection
- Feature engineering
- Machine Learning deployment
- Streamlit application development

Because apparently the modern internet needed a machine learning model to explain why  

`google-login-secure-paypal-free-money.xyz`

might not be trustworthy.
