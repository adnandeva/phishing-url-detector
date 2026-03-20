import pandas as pd

# Step 1: Load dataset
data = pd.read_csv("dataset/malicious_phish.csv")

# Step 2: Reduce size (keep it manageable)
data = data.sample(20000)

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
        'has_https': 1 if 'https' in url else 0,
        'num_digits': sum(c.isdigit() for c in url),
        'num_special': sum(not c.isalnum() for c in url)
    }

# Apply feature extraction
features = data['url'].apply(extract_features)

# Convert to DataFrame
features_df = pd.DataFrame(list(features), index=data.index)

# Combine with labels
final_data = pd.concat([features_df, data['label']], axis=1)

print(final_data.head())
print(final_data.shape)