# ❤️ AI Heart Disease Predictor

A smart AI-powered web application that predicts the risk of heart disease using Machine Learning models and real-time user input.

---

## 🚀 Features

* 🔍 Predicts **Low / Medium / High Risk**
* 📊 Displays **probability score**
* 🎯 Uses trained ML models for accurate prediction
* 🧑‍⚕️ Considers multiple health + lifestyle factors
* ⚡ Fast and interactive UI using Streamlit

---

## 🧠 Machine Learning Models Used

The system was trained and evaluated using multiple models:

* 🌳 Random Forest Classifier
* ⚡ XGBoost Classifier
* 📈 Logistic Regression
* 🔍 Support Vector Machine (SVM)
* 📊 K-Nearest Neighbors (KNN)

👉 Final model selected based on best accuracy and performance.

---

## ⚙️ Data Processing & Techniques

* 📌 Feature Engineering (age groups, interactions, etc.)
* 📌 Feature Scaling using StandardScaler
* 📌 Power Transformation for normalization
* 📌 Handling missing/noisy data
* 📌 Model comparison using cross-validation

---

## 📊 Input Features

* Age
* Gender
* Cholesterol
* Blood Pressure
* Max Heart Rate
* Smoking
* Diabetes
* Obesity
* Exercise Level
* Stress Level
* Family History

---

## 📌 Output

* ✅ Low Risk
* ⚠️ Medium Risk
* ❌ High Risk
* 📈 Probability Score (0–100%)

---

## 🧠 Tech Stack

* Python
* Streamlit
* Scikit-learn
* XGBoost
* Pandas
* NumPy

---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

---


---

## 📁 Project Structure

```
heart-disease-predictor/
│
├── app.py
├── model.pkl
├── scaler.pkl
├── features.pkl
├── requirements.txt
├── README.md
```

---

## 💡 Future Improvements

* 🔬 Add Explainable AI (SHAP / LIME)
* 📱 Mobile-friendly UI
* ☁️ API deployment (FastAPI)
* 🧾 Patient report generation

---

## 👨‍💻 Author

**PRADYUMN PARASHAR**

---

⭐ If you like this project, give it a star!
