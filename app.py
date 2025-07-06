import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

# Load trained model
model = joblib.load("med_refill_model.pkl")

st.set_page_config(page_title="Medication Refill Risk Predictor", layout="centered")
st.title("💊 Medication Refill Risk Predictor")
st.write("Predict whether a chronic patient will refill their prescription in the next 7 days.")

# Input form
with st.form("refill_form"):
    days_since_last_refill = st.slider("Days Since Last Refill", 0, 60, 15)
    age = st.slider("Age", 18, 80, 45)
    gender = st.selectbox("Gender", ["Female", "Male"])
    insurance_status = st.selectbox("Insurance Status", ["No", "Yes"])
    sms_reminder_sent = st.selectbox("SMS Reminder Sent?", ["No", "Yes"])
    num_past_late_refills = st.slider("Number of Past Late Refills", 0, 10, 1)
    condition_type = st.selectbox("Chronic Condition", ["Diabetes", "Hypertension", "Both"])
    avg_monthly_refills = st.slider("Avg Monthly Refills", 0.5, 2.0, 1.0, step=0.1)
    submitted = st.form_submit_button("Predict")

if submitted:
    # Convert inputs
    gender = 0 if gender == "Female" else 1
    insurance_status = 1 if insurance_status == "Yes" else 0
    sms_reminder_sent = 1 if sms_reminder_sent == "Yes" else 0
    condition_map = {"Diabetes": 0, "Hypertension": 1, "Both": 2}
    condition_type = condition_map[condition_type]

    input_data = pd.DataFrame([{
        'days_since_last_refill': days_since_last_refill,
        'age': age,
        'gender': gender,
        'insurance_status': insurance_status,
        'sms_reminder_sent': sms_reminder_sent,
        'num_past_late_refills': num_past_late_refills,
        'condition_type': condition_type,
        'avg_monthly_refills': avg_monthly_refills
    }])

    prediction = model.predict(input_data)[0]
    proba = model.predict_proba(input_data)[0][1]  # probability of refill

    st.subheader("🧠 Prediction")
    if prediction == 1:
        st.success("✅ Likely to Refill")
    else:
        st.error("❌ At Risk of Missing Refill")

    st.metric("Refill Likelihood", f"{proba * 100:.1f}%")

    st.subheader("📊 Patient Profile Summary")
    st.bar_chart(input_data.T)

    st.subheader("📉 Feature Importance (Logistic Regression)")
    coeffs = model.coef_[0]
    features = input_data.columns

    fig, ax = plt.subplots()
    ax.barh(features, coeffs)
    ax.set_title("Feature Importance")
    st.pyplot(fig)

    st.subheader("📥 Download Prediction")
    result_df = input_data.copy()
    result_df["Prediction"] = "Likely to Refill" if prediction == 1 else "At Risk"
    result_df["Confidence (%)"] = f"{proba * 100:.1f}%"
    csv = result_df.to_csv(index=False).encode("utf-8")
    st.download_button("Download CSV", data=csv, file_name="refill_prediction.csv", mime="text/csv")

