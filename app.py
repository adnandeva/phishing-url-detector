import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Title
st.title("Phishing URL Detector")

# Input box
url_input = st.text_input("Enter a URL:")

# Feature extraction function
def extract_features(url):
    return {
        'url_length': len(url),
        'num_dots': url.count('.'),
        'has_https': 1 if url.startswith("https") else 0,
        'num_digits': sum(c.isdigit() for c in url),
        'num_special': sum(not c.isalnum() for c in url)
    }

# Load and train model (same logic)
@st.cache_data
def load_model():
    data = pd.read_csv("dataset/malicious_phish.csv")
    data = data.sample(20000, random_state=42)
    data['label'] = data['type'].apply(lambda x: 0 if x == 'benign' else 1)
    data = data[['url', 'label']]

    features = data['url'].apply(extract_features)
    features_df = pd.DataFrame(list(features), index=data.index)
    final_data = pd.concat([features_df, data['label']], axis=1)

    X = final_data.drop('label', axis=1)
    y = final_data['label']

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)

    return model

model = load_model()

# Predict button
if st.button("Check URL"):
    
    if url_input:
        if not url_input.startswith("http"):
            url_input = "http://" + url_input

        features = extract_features(url_input) 
        df = pd.DataFrame([features])

        prediction = model.predict(df)[0]

        if prediction == 1:
            st.error("⚠️ This URL is likely PHISHING")
        else:
            st.success("✅ This URL looks SAFE")