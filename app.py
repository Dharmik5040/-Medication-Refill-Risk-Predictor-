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
if submitted:
    # Convert categorical inputs
    gender = 0 if gender == "Female" else 1
    insurance_status = 1 if insurance_status == "Yes" else 0
    sms_reminder_sent = 1 if sms_reminder_sent == "Yes" else 0
    condition_map = {"Diabetes": 0, "Hypertension": 1, "Both": 2}
    condition_type = condition_map[condition_type]

    # Prepare input data
    input_data = pd.DataFrame([[
        days_since_last_refill,
        age,
        gender,
        insurance_status,
        sms_reminder_sent,
        num_past_late_refills,
        condition_type,
        avg_monthly_refills
    ]], columns=[
        'days_since_last_refill',
        'age',
        'gender',
        'insurance_status',
        'sms_reminder_sent',
        'num_past_late_refills',
        'condition_type',
        'avg_monthly_refills'
    ])

    # Predict
    prediction = model.predict(input_data)[0]

    # Display result
    st.subheader("Prediction:")
    if prediction == 1:
        st.success("✅ Likely to Refill")
    else:
        st.error("❌ At Risk of Missing Refill")
