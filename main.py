import pandas as pd

# Step 1: Load dataset
data = pd.read_csv("dataset/malicious_phish.csv")

# Step 2: Reduce size (keep it manageable)
data = data.sample(20000, random_state=42)

# Step 3: Convert labels
# benign → 0 (safe)
# others → 1 (malicious)
data['label'] = data['type'].apply(lambda x: 0 if x == 'benign' else 1)

# Step 4: Keep only required columns
data = data[['url', 'label']]

# Check output
#print(data.head())
#print(data.shape)

# Step 5: Feature extraction

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

# Apply feature extraction
features = data['url'].apply(extract_features)

# Convert to DataFrame
features_df = pd.DataFrame(list(features), index=data.index)

# Combine with labels
final_data = pd.concat([features_df, data['label']], axis=1)

#print(final_data.head())
#print(final_data.shape)

# Step 6: Separate features and label

X = final_data.drop('label', axis=1)
y = final_data['label']

# Check
#print("Features (X):")
#print(X.head())

#print("\nLabels (y):")
#print(y.head())

# Step 7: Train-test split

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Check
#print("Training set size:", X_train.shape)
#print("Testing set size:", X_test.shape)

# Step 8: Train model

from sklearn.linear_model import LogisticRegression

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Step 9: Predict

y_pred = model.predict(X_test)

# Step 10: Check accuracy

from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, y_pred)
print("Model Accuracy:", accuracy)

# Step 11: Detailed evaluation

from sklearn.metrics import classification_report, confusion_matrix

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Step 12: Random Forest model

from sklearn.ensemble import RandomForestClassifier

rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

rf_pred = rf_model.predict(X_test)

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

rf_accuracy = accuracy_score(y_test, rf_pred)
print("\nRandom Forest Accuracy:", rf_accuracy)

print("\nRandom Forest Classification Report:")
print(classification_report(y_test, rf_pred))

print("\nRandom Forest Confusion Matrix:")
print(confusion_matrix(y_test, rf_pred))