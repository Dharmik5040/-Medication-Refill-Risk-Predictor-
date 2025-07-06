# 💊 Medication Refill Risk Predictor

This Streamlit app predicts whether a patient is likely to refill their chronic medication (e.g., for diabetes, hypertension) within the next 7 days based on their past behavior and profile data.

🔗 **Live App**: [Click to try it out](https://fkjnndufh3ywech2nbtkrh.streamlit.app/)

---

## 🧠 Problem Statement

Chronic patients often miss medication refills, leading to poor health outcomes and increased hospitalization. This tool helps pharmacies or care managers identify patients who are at risk of missing their refill window, enabling proactive intervention.

---

## 🛠️ Features Used

- `days_since_last_refill`
- `age`
- `gender`
- `insurance_status`
- `sms_reminder_sent`
- `num_past_late_refills`
- `condition_type` (Diabetes / Hypertension / Both)
- `avg_monthly_refills`

🎯 **Target**: `refilled_within_7_days`

---

## 🤖 Model

- **Model Used**: Logistic Regression
- **Trained on**: Simulated dataset of 300 patients
- **Accuracy**: ~80% (based on train/test split)

---

## 📂 Project Structure
├── app.py # Streamlit app script
├── med_refill_model.pkl # Trained ML model
├── med_refill_dataset.csv # Simulated patient dataset
├── requirements.txt # Dependencies for Streamlit Cloud
## 👨‍⚕️ Built By

**Dharmik Shah** — Healthcare + Pharmacy + AI  
🔗 [LinkedIn](www.linkedin.com/in/dharmikshah4)  
📫 dharmik5040@gmail.com

---

## 🧠 Future Improvements

- Integrate with real pharmacy refill APIs  
- Alert system for patients at high risk  
- Train on real-world datasets with richer features
