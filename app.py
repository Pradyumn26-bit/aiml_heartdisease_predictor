import streamlit as st
import pandas as pd
import pickle
import numpy as np

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="AI Heart Disease Predictor",
    page_icon="❤️",
    layout="wide"
)

# ---------------- LOAD ----------------
model = pickle.load(open("model.pkl", "rb"))
features = pickle.load(open("features.pkl", "rb"))

# OPTIONAL SCALER
try:
    scaler = pickle.load(open("scaler.pkl", "rb"))
except:
    scaler = None

# ---------------- HEADER ----------------
st.title("❤️ AI Heart Disease Predictor")
st.markdown("### Smart Health Risk Analysis System")

# ---------------- INPUT ----------------
col1, col2 = st.columns(2)

with col1:
    age = st.slider("Age", 20, 100, 50)
    sex = st.selectbox("Gender", ["Male", "Female"])
    sex = 1 if sex == "Male" else 0

    smoking = st.selectbox("Smoking", ["No", "Yes"])
    smoking = 1 if smoking == "Yes" else 0

    diabetes = st.selectbox("Diabetes", ["No", "Yes"])
    diabetes = 1 if diabetes == "Yes" else 0

    obesity = st.selectbox("Obesity", ["No", "Yes"])
    obesity = 1 if obesity == "Yes" else 0

with col2:
    cholesterol = st.slider("Cholesterol", 100, 350, 200)
    resting_bp = st.slider("Blood Pressure", 80, 200, 120)
    max_hr = st.slider("Max Heart Rate", 60, 220, 150)

    exercise = st.selectbox("Exercise Level", [0,1,2])
    stress = st.selectbox("Stress Level", [0,1,2])

    family = st.selectbox("Family History", ["No", "Yes"])
    family = 1 if family == "Yes" else 0

# ---------------- INPUT DATA ----------------
input_dict = {
    "age": age,
    "sex": sex,
    "cholesterol": cholesterol,
    "resting_bp": resting_bp,
    "max_heart_rate": max_hr,
    "smoking": smoking,
    "diabetes": diabetes,
    "obesity": obesity,
    "exercise_level": exercise,
    "stress_level": stress,
    "family_history": family
}

input_df = pd.DataFrame([input_dict])

# ---------------- MATCH FEATURES ----------------
for col in features:
    if col not in input_df.columns:
        input_df[col] = 0

input_df = input_df[features]

# ---------------- SCALE ----------------
if scaler is not None:
    input_df = scaler.transform(input_df)

# ---------------- PREDICT ----------------
if st.button("🔍 Predict Risk"):

    pred = model.predict(input_df)[0]

    try:
        prob = model.predict_proba(input_df)[0][1]
    except:
        prob = float(pred)

    if prob < 0.3:
        st.success(f"Low Risk ({prob:.2%})")
    elif prob < 0.7:
        st.warning(f"Medium Risk ({prob:.2%})")
    else:
        st.error(f"High Risk ({prob:.2%})")

    st.progress(int(prob * 100))
