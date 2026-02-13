import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Title
st.title("📊 Customer Churn Prediction App")

# Load dataset
df = pd.read_csv("Telco_Churn_dataset.csv")

# Features & Target
X = df.drop("churn", axis=1)
y = df["churn"]

# Train model
model = RandomForestClassifier(random_state=42)
model.fit(X, y)

st.subheader("Enter Key Customer Details:")

# 🔹 Professional Inputs (Sliders + Dropdown)
tenure = st.slider("Tenure (months)", 0, 72, 12)
age = st.slider("Age", 18, 80, 30)
income = st.slider("Income", 0, 200, 50)

employ_option = st.selectbox("Employment Status", ["No", "Yes"])
employ = 1 if employ_option == "Yes" else 0

longmon = st.slider("Monthly Long Distance Charges", 0, 200, 20)
longten = st.slider("Total Long Distance Charges", 0, 1000, 100)

# Prediction
if st.button("Predict Churn"):

    input_data = {
        'tenure': tenure,
        'age': age,
        'income': income,
        'employ': employ,
        'longmon': longmon,
        'longten': longten
    }

    input_df = pd.DataFrame([input_data])

    # Add missing columns as 0
    for col in X.columns:
        if col not in input_df.columns:
            input_df[col] = 0

    # Reorder columns
    input_df = input_df[X.columns]

    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    # Result Display
    st.write(f"📊 Churn Probability: {round(probability * 100, 2)}%")

    if probability > 0.7:
        st.error("🔴 High Risk: This customer is likely to churn.")
    elif probability > 0.4:
        st.warning("🟡 Medium Risk: Customer may churn.")
    else:
        st.success("🟢 Low Risk: This customer is likely to stay.")


