import streamlit as st
import pandas as pd
import numpy as np
import pickle

# ==============================
# PAGE SETTINGS
# ==============================
st.set_page_config(page_title="Insurance Premium Predictor", layout="centered")

st.title("💰 Insurance Premium Predictor")
st.write("Enter details to estimate insurance premium")

# ==============================
# LOAD MODEL + COLUMNS
# ==============================
model = pickle.load(open("model.pkl", "rb"))
training_cols = pickle.load(open("columns.pkl", "rb"))

# ==============================
# USER INPUTS
# ==============================
age = st.slider("Age", 18, 80, 30)
income = st.number_input("Annual Income", value=500000)
credit_score = st.slider("Credit Score", 300, 900, 650)
health_score = st.slider("Health Score", 0, 100, 50)
dependents = st.number_input("Number of Dependents", 0, 10, 2)
claims = st.number_input("Previous Claims", 0, 20, 1)
vehicle_age = st.slider("Vehicle Age", 0, 20, 5)
insurance_duration = st.slider("Insurance Duration (years)", 1, 20, 5)
smoking = st.selectbox("Smoking Status", ["No", "Yes"])

# ==============================
# FEATURE ENGINEERING
# ==============================
smoking_flag = 1 if smoking == "Yes" else 0

risk_score = claims * 2 + smoking_flag * 3 + health_score
income_per_dependent = income / (dependents + 1)
claims_per_year = claims / (insurance_duration + 1)
health_claim_interaction = health_score * claims

# ==============================
# CREATE INPUT DATAFRAME (FIXED)
# ==============================

# Create empty dataframe with ALL training columns
input_data = pd.DataFrame(columns=training_cols)

# Initialize row
input_data.loc[0] = 0

# Fill known features
input_data['Age'] = age
input_data['Annual_Income'] = income
input_data['Credit_Score'] = credit_score
input_data['Health_Score'] = health_score
input_data['Number_of_Dependents'] = dependents
input_data['Previous_Claims'] = claims
input_data['Vehicle_Age'] = vehicle_age
input_data['Insurance_Duration'] = insurance_duration

# Engineered features
input_data['smoking_flag'] = smoking_flag
input_data['risk_score'] = risk_score
input_data['income_per_dependent'] = income_per_dependent
input_data['claims_per_year'] = claims_per_year
input_data['health_claim_interaction'] = health_claim_interaction

# ==============================
# PREDICTION
# ==============================
if st.button("Predict Premium"):
    prediction = model.predict(input_data)[0]
    st.success(f"💰 Estimated Premium: ₹ {round(prediction, 2)}")
    