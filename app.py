import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("med_refill_model.pkl")

st.title("💊 Medication Refill Risk Predictor")
st.write("This app predicts if a patient will refill their chronic prescription within 7 days.")

# User input form
with st.form("refill_form"):
    days_since_last_refill = st.slider("Days Since Last Refill", 0, 60, 15)
    age = st.slider("Age", 18, 80, 45)
    gender = st.selectbox("Gender", ["Female", "Male"])
    insurance_status = st.selectbox("Insurance Status", ["No", "Yes"])
    sms_reminder_sent = st.selectbox("SMS Reminder Sent?", ["No", "Yes"])
    num_past_late_refills = st.slider("Number of Past Late Refills", 0, 10, 1)
    condition_type = st.selectbox("Chronic Condition", ["Diabetes", "Hypertension", "Both"])
    avg_mon_
with st.form("refill_form"):
    days_since_last_refill = st.slider("Days Since Last Refill", 0, 60, 15)
    age = st.slider("Age", 18, 80, 45)
    gender = st.selectbox("Gender", ["Female", "Male"])
    insurance_status = st.selectbox("Insurance Status", ["No", "Yes"])
    sms_reminder_sent = st.selectbox("SMS Reminder Sent?", ["No", "Yes"])
    num_past_late_refills = st.slider("Number of Past Late Refills", 0, 10, 1)
    condition_type = st.selectbox("Chronic Condition", ["Diabetes", "Hypertension", "Both"])
    avg_monthly_refills = st.slider("Avg Monthly Refills", 0.5, 2.0, 1.0, step=0.1)

    # ✅ Add this inside the form:
    submitted = st.form_submit_button("Predict")
