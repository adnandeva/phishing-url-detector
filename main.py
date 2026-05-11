import re
import joblib
import pandas as pd

from urllib.parse import urlparse

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
# LOAD DATASET
# =========================

data = pd.read_csv(
    "dataset/phishing_url_dataset_unique.csv"
)

# Keep only required columns

data = data[['url', 'label']]

# Remove missing values

data = data.dropna(
    subset=['url', 'label']
)

# Convert labels safely

data['label'] = pd.to_numeric(
    data['label'],
    errors='coerce'
)

# Remove invalid labels

data = data.dropna(
    subset=['label']
)

# Convert label to integer

data['label'] = data['label'].astype(int)

# Shuffle dataset

data = data.sample(
    frac=1,
    random_state=42
).reset_index(drop=True)

# Use subset for faster training

data = data.sample(
    20000,
    random_state=42
).reset_index(drop=True)

# =========================
# FEATURE EXTRACTION
# =========================

def extract_features(url):

    parsed = urlparse(url)

    hostname = parsed.netloc.lower()

    suspicious_words = [

        'login',

        'verify',

        'account',

        'secure',

        'update',

        'bank',

        'signin',

        'password',

        'confirm',

        'wallet',

        'crypto',

        'paypal'

    ]

    ip_pattern = r'(\d{1,3}\.){3}\d{1,3}'

    return {

        'url_length': len(url),

        'num_dots': url.count('.'),

        'num_digits': sum(
            c.isdigit()
            for c in url
        ),

        'num_special': sum(
            not c.isalnum()
            for c in url
        ),

        'has_ip': 1 if re.search(
            ip_pattern,
            hostname
        ) else 0,

        'has_hyphen': 1 if '-' in hostname else 0,

        'num_subdomains': max(
            hostname.count('.') - 1,
            0
        ),

        'has_suspicious_words': 1 if any(

            word in url.lower()

            for word in suspicious_words

        ) else 0,

        'uses_https': 1 if parsed.scheme == 'https' else 0
    }

# =========================
# CREATE FEATURE DATAFRAME
# =========================

feature_rows = []

for url in data['url']:

    feature_rows.append(
        extract_features(url)
    )

features_df = pd.DataFrame(
    feature_rows
)

# Reset indexes BEFORE concat

features_df = features_df.reset_index(
    drop=True
)

labels_df = data[['label']].reset_index(
    drop=True
)

# Combine safely

final_data = pd.concat(
    [features_df, labels_df],
    axis=1
)

# Final NaN cleanup

final_data = final_data.dropna()

# =========================
# SPLIT FEATURES & LABELS
# =========================

X = final_data.drop(
    'label',
    axis=1
)

y = final_data['label']

# =========================
# TRAIN TEST SPLIT
# =========================

X_train, X_test, y_train, y_test = train_test_split(

    X,
    y,

    test_size=0.2,

    random_state=42,

    stratify=y
)

# =========================
# LOGISTIC REGRESSION
# =========================

lr_model = LogisticRegression(
    max_iter=1000
)

lr_model.fit(
    X_train,
    y_train
)

lr_pred = lr_model.predict(
    X_test
)

print("\nLogistic Regression Accuracy:")

print(
    accuracy_score(
        y_test,
        lr_pred
    )
)

# =========================
# DECISION TREE
# =========================

dt_model = DecisionTreeClassifier(
    random_state=42
)

dt_model.fit(
    X_train,
    y_train
)

dt_pred = dt_model.predict(
    X_test
)

print("\nDecision Tree Accuracy:")

print(
    accuracy_score(
        y_test,
        dt_pred
    )
)

# =========================
# RANDOM FOREST
# =========================

rf_model = RandomForestClassifier(

    n_estimators=300,

    max_depth=20,

    min_samples_split=5,

    min_samples_leaf=2,

    class_weight='balanced',

    random_state=42,

    n_jobs=-1
)

rf_model.fit(
    X_train,
    y_train
)

rf_pred = rf_model.predict(
    X_test
)

# =========================
# EVALUATION
# =========================

print("\nRandom Forest Accuracy:")

print(
    accuracy_score(
        y_test,
        rf_pred
    )
)

print("\nRandom Forest Classification Report:")

print(
    classification_report(
        y_test,
        rf_pred
    )
)

print("\nRandom Forest Confusion Matrix:")

print(
    confusion_matrix(
        y_test,
        rf_pred
    )
)

# =========================
# FEATURE IMPORTANCE
# =========================

print("\nFeature Importance:")

feature_names = X.columns

importances = rf_model.feature_importances_

for name, score in zip(
    feature_names,
    importances
):

    print(
        f"{name:<25} {score:.4f}"
    )

# =========================
# SAVE MODEL
# =========================

joblib.dump(
    rf_model,
    "model.pkl"
)

print("\nModel saved as model.pkl")