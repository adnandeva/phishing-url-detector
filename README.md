# Phishing URL Detection using Lexical Analysis

## Overview
This project detects whether a URL is legitimate or malicious using lexical features extracted directly from the URL string. This approach does not require accessing webpage content, making it fast and lightweight. This makes the system efficient and suitable for real-time detection scenarios.

## How it Works
- URLs are loaded from a labeled dataset  
- Labels are converted into binary (0 = legit, 1 = malicious)
- Lexical features are extracted from URLs:
  - URL length  
  - Number of dots  
  - Presence of HTTPS  
  - Number of digits  
  - Special characters  

## Tech Stack
- Python (Pandas for data processing)

## Project Status
Preprocessing and feature extraction completed.  
Model training will be added next.

## Future Improvements
- Train and evaluate machine learning models  
- Improve feature engineering  
- Add real-time URL prediction  

## Author
Adnan Riyaz – Computer Science Student
