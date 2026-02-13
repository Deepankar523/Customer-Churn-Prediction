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
model = RandomForestClassifier()
model.fit(X, y)

st.subheader("Enter Key Customer Details:")

# 🔹 Only important inputs (reduced from 28 to 6)
tenure = st.number_input("Tenure (months)", min_value=0.0)
age = st.number_input("Age", min_value=18.0)
income = st.number_input("Income", min_value=0.0)
employ = st.number_input("Employment Status (0 = No, 1 = Yes)", min_value=0.0, max_value=1.0)
longmon = st.number_input("Monthly Long Distance Charges", min_value=0.0)
longten = st.number_input("Total Long Distance Charges", min_value=0.0)

# Prediction
if st.button("Predict Churn"):

    # Create dataframe with selected inputs
    input_data = {
        'tenure': tenure,
        'age': age,
        'income': income,
        'employ': employ,
        'longmon': longmon,
        'longten': longten
    }

    input_df = pd.DataFrame([input_data])

    # 🔹 Add missing columns as 0 (important for model compatibility)
    for col in X.columns:
        if col not in input_df.columns:
            input_df[col] = 0

    # Reorder columns to match training data
    input_df = input_df[X.columns]

    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    if prediction == 1:
        st.error("⚠️ This customer is likely to churn.")
    else:
        st.success("✅ This customer is likely to stay.")

    st.write(f"📊 Churn Probability: {round(probability * 100, 2)}%")

