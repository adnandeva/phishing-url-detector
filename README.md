# 🔐 Phishing URL Detection using Machine Learning

## Overview
This project detects whether a URL is legitimate or phishing using machine learning.

It uses **lexical features extracted directly from the URL**, making it fast and lightweight without accessing webpage content.

An interactive web app is built using Streamlit for real-time predictions.

---

## 🚀 Live Demo
👉 https://phishing-detector-adnan.streamlit.app

---

## ✨ Features
- URL length analysis  
- Number of dots & subdomains  
- Detection of IP-based URLs  
- Count of digits and special characters  
- HTTPS presence check  
- Detection of suspicious keywords (login, verify, secure, update, etc.)  

---

## 🧠 Models Used
- Logistic Regression (baseline model)  
- Decision Tree (rule-based comparison)  
- Random Forest (final deployed model)  

---

## 📊 Results

### Model Performance

| Model               | Accuracy |
|--------------------|---------|
| Logistic Regression | 75.17%  |
| Decision Tree       | 83.6%   |
| Random Forest       | 85.32%  |

### 🔍 Random Forest (Final Model)

- Precision (Phishing): **0.76**
- Recall (Phishing): **0.81**
- F1 Score: **0.79**

The Random Forest model significantly improves phishing detection, especially recall (catching more malicious URLs).

---

### 📈 Feature Importance (Random Forest)

- URL length: **0.19**
- Number of dots: **0.17**
- Number of special characters: **0.27** *(most important)*
- Number of digits: **0.13**
- Number of subdomains: **0.15**
- HTTPS presence: **0.04**
- IP address presence: **0.02**
- Suspicious keywords: **0.03**

This shows that structural complexity of URLs (length, symbols, dots) plays a major role in identifying phishing links.

---

## ⚙️ Key Improvements
- Added advanced lexical features for better detection  
- Improved phishing recall using class balancing  
- Tuned Random Forest for better generalization  
- Saved trained model using `joblib` (no retraining in UI)  
- Built interactive Streamlit UI with:
  - Confidence score  
  - Visual feedback  
  - Explanation of predictions  

---

## 🛠 Tech Stack
- Python *(core programming language)*  
- Pandas *(data processing and manipulation)*  
- Scikit-learn *(machine learning models)*  
- Streamlit *(web app UI)*  
- Joblib *(model saving and loading)*  

---

## ▶️ How to Run Locally

1. Clone the repository  
```bash
git clone https://github.com/adnandeva/phishing-url-detector.git
cd phishing-url-detector
```

2. Create a virtual environment  
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies  
```bash
pip install -r requirements.txt
```

4. Run the app  
```bash
streamlit run app.py
```

---

## 📂 Project Structure
```
phishing-url-detector/
│── app.py            # Streamlit UI  
│── main.py           # Model training script  
│── model.pkl         # Saved trained model  
│── dataset/          # Dataset files  
│── requirements.txt  
│── README.md  
```

---

## 📌 Future Improvements
- Add whitelist for trusted domains (Google, Amazon, etc.)  
- Improve feature engineering  
- Try advanced models (XGBoost, Gradient Boosting)  
- Enhance UI/UX further  

---

## 👤 Author
Adnan Riyaz  
Pre-Final Year Computer Science Student  
Ramaiah University of Applied Sciences
