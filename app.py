import re
import streamlit as st
import pandas as pd
import joblib

from urllib.parse import urlparse

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Phishing URL Detector",
    page_icon="🔐",
    layout="centered"
)

# =========================
# TRUSTED DOMAINS
# =========================

TRUSTED_DOMAINS = [

    'google.com',

    'github.com',

    'amazon.com',

    'microsoft.com',

    'apple.com',

    'linkedin.com',

    'youtube.com',

    'nasa.gov'
]

# =========================
# URL NORMALIZATION
# =========================

def normalize_url(url):

    url = str(url).strip().lower()

    if not url.startswith(
        ('http://', 'https://')
    ):

        url = 'https://' + url

    return url

# =========================
# TRUSTED DOMAIN CHECK
# =========================

def is_trusted_domain(url):

    parsed = urlparse(url)

    domain = parsed.netloc.lower()

    domain = domain.replace(
        'www.',
        ''
    )

    return domain in TRUSTED_DOMAINS

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
# LOAD MODEL
# =========================

@st.cache_resource
def load_model():

    return joblib.load(
        "model.pkl"
    )

model = load_model()

# =========================
# UI
# =========================

st.title(
    "🔐 Phishing URL Detector"
)

st.caption(
    "Machine Learning based phishing URL analysis"
)

url_input = st.text_input(
    "Enter URL",
    placeholder="e.g. google.com"
)

analyze = st.button(
    "🔍 Analyze URL"
)

# =========================
# PREDICTION
# =========================

if analyze:

    if url_input:

        url_input = normalize_url(
            url_input
        )

        # Trusted whitelist

        if is_trusted_domain(
            url_input
        ):

            st.success(
                "✅ Trusted Domain"
            )

            st.write(
                "This domain exists in the trusted whitelist."
            )

            st.progress(0.01)

            st.write(
                "1% phishing probability"
            )

        else:

            with st.spinner(
                "Analyzing URL..."
            ):

                features = extract_features(
                    url_input
                )

                df = pd.DataFrame(
                    [features]
                )

                prediction = model.predict(df)[0]

                probability = model.predict_proba(df)[0][1]

            # Result

            if prediction == 1:

                st.error(
                    "🚨 Likely Phishing URL"
                )

            else:

                st.success(
                    "✅ URL appears safe"
                )

            # Confidence

            st.subheader(
                "Confidence Score"
            )

            st.progress(
                float(probability)
            )

            st.write(
                f"{probability * 100:.2f}% phishing probability"
            )

            # Analysis

            st.subheader(
                "Detected Indicators"
            )

            reasons = []

            if features['has_ip']:

                reasons.append(
                    "Uses IP address instead of domain"
                )

            if features['has_hyphen']:

                reasons.append(
                    "Contains hyphenated domain"
                )

            if features['num_digits'] > 5:

                reasons.append(
                    "Contains many digits"
                )

            if features['num_special'] > 10:

                reasons.append(
                    "Contains excessive special characters"
                )

            if features['num_dots'] > 3:

                reasons.append(
                    "Contains many subdomains/dots"
                )

            if features['url_length'] > 75:

                reasons.append(
                    "URL is unusually long"
                )

            if features['has_suspicious_words']:

                reasons.append(
                    "Contains phishing-related keywords"
                )

            if reasons:

                for reason in reasons:

                    st.write(
                        f"• {reason}"
                    )

            else:

                st.write(
                    "No major suspicious indicators detected."
                )

        st.markdown("---")

        st.caption(
            "Built by Adnan using Python, Scikit-learn, and Streamlit"
        )

    else:

        st.warning(
            "Please enter a URL."
        )