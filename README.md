# Smart-premium-
# 💰 Insurance Premium Prediction System

## 📌 Project Overview

This project aims to build a machine learning model that predicts **insurance premium amounts** based on customer details such as age, income, health condition, and claim history.

The solution includes:

* Data preprocessing and cleaning
* Feature engineering
* Model training using LightGBM
* Evaluation of model performance
* Deployment using Streamlit for real-time predictions

---

## 🎯 Problem Statement

Insurance companies need accurate premium estimation to:

* Assess risk efficiently
* Provide fair pricing
* Improve customer satisfaction

This project builds a predictive system to estimate premiums using data-driven techniques.

---

## 📊 Dataset Description

The dataset contains **1.2 million records** with 20+ features:

### 🔹 Key Features

* Age
* Gender
* Annual Income
* Marital Status
* Number of Dependents
* Health Score
* Previous Claims
* Credit Score
* Insurance Duration
* Vehicle Age
* Smoking Status
* Exercise Frequency
* Policy Type

### 🎯 Target Variable

* **Premium Amount**

---

## ⚙️ Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* LightGBM
* Streamlit
* Matplotlib

---

## 🔄 Project Workflow

### 1️⃣ Data Preprocessing

* Handled missing values using median/mode
* Converted date features
* Removed irrelevant columns

### 2️⃣ Feature Engineering

Created new meaningful features:

* `risk_score`
* `income_per_dependent`
* `claims_per_year`
* `health_claim_interaction`

### 3️⃣ Encoding

* Applied one-hot encoding for categorical variables

### 4️⃣ Model Training

* Used **LightGBM Regressor**
* Trained on sampled dataset (200k rows)

### 5️⃣ Evaluation Metrics

* RMSE (Root Mean Squared Error)
* R² Score

---

## 📈 Model Performance

| Metric   | Value |
| -------- | ----- |
| RMSE     | ~850  |
| R² Score | ~0.04 |

📌 Note: The dataset has weak feature-target correlation, so performance is limited.

---

## 📊 Feature Importance

Top contributing features:

* Annual Income
* Credit Score
* Health Score
* Risk Score
* Age

---

## 🌐 Streamlit Application

### Features:

* User-friendly interface
* Real-time prediction
* Dynamic input fields

### ▶️ Run the App

```bash
streamlit run app.py
```
## 🚀 How to Run the Project

1. Clone the repository

```bash
git clone <your-repo-link>
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run training script (optional)

4. Launch Streamlit app

```bash
streamlit run app.py
```

## 🧠 Key Learnings

* Handling large-scale datasets
* Feature engineering for better prediction
* Managing real-world ML pipeline issues
* Deploying ML models using Streamlit

--

## 📌 Future Improvements

* Hyperparameter tuning
* Advanced feature selection
* Model ensemble techniques
* Cloud deployment

---

## 👩‍💻 Author

Rajalakshmi

---
