import re
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

# =========================
# DATA LOADING
# =========================

data = pd.read_csv("dataset/malicious_phish.csv")

# Reduce dataset size for faster training
data = data.sample(20000, random_state=42)

# Convert labels:
# benign -> 0 (safe)
# others -> 1 (malicious)
data['label'] = data['type'].apply(
    lambda x: 0 if x == 'benign' else 1
)

# Keep only required columns
data = data[['url', 'label']]

# =========================
# FEATURE EXTRACTION
# =========================

def extract_features(url):

    # Detect IP-based URLs
    ip_pattern = r'\d+\.\d+\.\d+\.\d+'
    has_ip = 1 if re.search(ip_pattern, url) else 0

    # Suspicious phishing keywords
    suspicious_words = [
        'login',
        'verify',
        'account',
        'secure',
        'update'
    ]

    return {
        'url_length': len(url),
        'num_dots': url.count('.'),
        'has_https': 1 if url.startswith("https") else 0,
        'num_digits': sum(c.isdigit() for c in url),
        'num_special': sum(not c.isalnum() for c in url),

        # Advanced lexical features
        'has_ip': has_ip,
        'num_subdomains': max(url.count('.') - 1, 0),

        'has_suspicious_words': 1 if any(
            word in url.lower()
            for word in suspicious_words
        ) else 0
    }

# Apply feature extraction
features = data['url'].apply(extract_features)

# Convert features into DataFrame
features_df = pd.DataFrame(
    list(features),
    index=data.index
)

# Combine features with labels
final_data = pd.concat(
    [features_df, data['label']],
    axis=1
)

# =========================
# DATA PREPARATION
# =========================

X = final_data.drop('label', axis=1)
y = final_data['label']

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# =========================
# LOGISTIC REGRESSION MODEL
# =========================

lr_model = LogisticRegression(max_iter=1000)

lr_model.fit(X_train, y_train)

lr_pred = lr_model.predict(X_test)

lr_accuracy = accuracy_score(y_test, lr_pred)

print("\nLogistic Regression Accuracy:")
print(lr_accuracy)

# =========================
# DECISION TREE MODEL
# =========================

dt_model = DecisionTreeClassifier(
    random_state=42
)

dt_model.fit(X_train, y_train)

dt_pred = dt_model.predict(X_test)

dt_accuracy = accuracy_score(y_test, dt_pred)

print("\nDecision Tree Accuracy:")
print(dt_accuracy)

# =========================
# RANDOM FOREST MODEL
# =========================

rf_model = RandomForestClassifier(
    n_estimators=200,
    max_depth=15,
    min_samples_split=5,
    min_samples_leaf=2,
    class_weight='balanced',
    random_state=42
)

rf_model.fit(X_train, y_train)

rf_pred = rf_model.predict(X_test)

rf_accuracy = accuracy_score(y_test, rf_pred)

print("\nRandom Forest Accuracy:")
print(rf_accuracy)

# =========================
# MODEL EVALUATION
# =========================

print("\nRandom Forest Classification Report:")
print(classification_report(y_test, rf_pred))

print("\nRandom Forest Confusion Matrix:")
print(confusion_matrix(y_test, rf_pred))

# =========================
# FEATURE IMPORTANCE
# =========================

print("\nFeature Importance:")

feature_names = X.columns
importances = rf_model.feature_importances_

for name, score in zip(feature_names, importances):
    print(f"{name:<25} {score:.4f}")

# =========================
# MODEL SAVING
# =========================

joblib.dump(rf_model, "model.pkl")

print("\nModel saved as model.pkl")