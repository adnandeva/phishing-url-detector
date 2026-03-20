# Phishing URL Detection using Machine Learning

## Overview
This project detects whether a URL is legitimate or phishing using machine learning. It uses lexical features extracted directly from the URL, making it fast and lightweight without needing to access webpage content.

---

## Features
- URL length
- Number of dots
- Number of digits
- Number of special characters
- HTTPS presence

---

## Models Used
- Logistic Regression (baseline)
- Random Forest (improved performance)

---

## Results
- Logistic Regression Accuracy: ~72%
- Random Forest Accuracy: ~85%

Random Forest significantly improves phishing detection performance, especially recall for malicious URLs.

---

## Tech Stack
- Python
- Pandas (data processing)
- Scikit-learn (machine learning)
- Streamlit (UI)

---

## How to Run

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

3.	Install dependencies
```bash
pip install -r requirements.txt
```

4.	Run the app
```bash
streamlit run app.py
```

---

## Author
Adnan Riyaz – Computer Science Student
