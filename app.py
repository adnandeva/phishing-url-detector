import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Title
st.title("Phishing URL Detector")

# Input box
url_input = st.text_input("Enter a URL:")

# Feature extraction

def extract_features(url):
    return {
        'url_length': len(url),
        'num_dots': url.count('.'),
        'has_https': 1 if url.startswith("https") else 0,
        'num_digits': sum(c.isdigit() for c in url),
        'num_special': sum(not c.isalnum() for c in url),

        # NEW FEATURES
        'has_ip': 1 if any(char.isdigit() for char in url.split('/')[0]) else 0,
        'num_subdomains': url.count('.') - 1,
        'has_suspicious_words': 1 if any(word in url.lower() for word in ['login', 'verify', 'account', 'secure', 'update']) else 0
    }

# Load model (no training anymore)
import joblib

@st.cache_resource
def load_model():
    return joblib.load("model.pkl")

model = load_model()

# Predict button

if st.button("Check URL"):

    if url_input:
        if not url_input.startswith("http"):
            url_input = "http://" + url_input

        # Extract features
        features = extract_features(url_input)
        df = pd.DataFrame([features])

        # Prediction
        prediction = model.predict(df)[0]
        probability = model.predict_proba(df)[0][1]  # phishing probability

        # Display result
        if prediction == 1:
            st.error("⚠️ This URL is likely PHISHING")
        else:
            st.success("✅ This URL looks SAFE")

        # Show probability
        st.subheader("Confidence Score")
        st.progress(int(probability * 100))
        st.write(f"Phishing Probability: {probability:.2f}")

        # Basic explanation
        st.subheader("Why this result?")

        reasons = []
        if features['num_digits'] > 5:
            reasons.append("Contains many digits")
        if features['num_special'] > 10:
            reasons.append("Contains many special characters")
        if features['num_dots'] > 3:
            reasons.append("Too many dots (suspicious structure)")
        if features['url_length'] > 75:
            reasons.append("URL is unusually long")

        if reasons:
            for r in reasons:
                st.write(f"- {r}")
        else:
            st.write("No obvious suspicious patterns detected")