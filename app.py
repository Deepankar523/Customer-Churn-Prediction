import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

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

st.subheader("Enter Customer Details:")

# Create input fields dynamically
input_data = {}
for column in X.columns:
    input_data[column] = st.number_input(f"{column}", value=0.0)

# Prediction
if st.button("Predict Churn"):
    input_df = pd.DataFrame([input_data])
    prediction = model.predict(input_df)[0]

    if prediction == 1:
        st.error("⚠️ This customer is likely to churn.")
    else:
        st.success("✅ This customer is likely to stay.")

    st.write(f"📊 Churn Probability: {round(probability * 100, 2)}%")
