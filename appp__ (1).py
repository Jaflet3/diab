# -*- coding: utf-8 -*-
"""appp__.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1j881N3tLxsWOieaS_TGCfGK8tjKOxZec
"""

# Commented out IPython magic to ensure Python compatibility.
# %pip install streamlit



# Commented out IPython magic to ensure Python compatibility.
# Install streamlit in the cell to ensure it's available
# %pip install streamlit --quiet



import numpy as np
import pickle

import streamlit as st
import numpy as np
import pickle

# Load the saved model
try:
    with open('model.pkl', 'rb') as file:
      model=pickle.load(file)
except FileNotFoundError:
    st.error("⚠️ Model file not found. Make sure 'model.pkl' is in the same folder.")
    st.stop()
except Exception as e:
    st.error(f"⚠️ Error loading model: {e}")
    st.stop()

st.title("🧬 Diabetes Risk Prediction")
st.write("Enter your health information below to check your diabetes risk:")

# Input fields
age = st.slider("Age (years)", 1, 100, 30)

bmi = st.number_input("Body Mass Index (BMI)", 10.0, 60.0, 25.0)

# Added height input as it seems to be missing based on input_data

weight = st.number_input("Weight (kg)", 50, 200, 70) # Corrected variable name and range

blood_glucose = st.number_input("Blood Glucose (mg/dL)", 50, 300, 100) # Added input for blood glucose


# Encoding inputs


# Prediction
if st.button("🔍 Predict Risk"):
    input_data = [[age,bmi,weight,blood_glucose]]
    prediction = model.predict(input_data) # Corrected variable name to 'model'
    if prediction[0] == 1:
            st.success("✅ Prediction: High Risk of Diabetes")
    else:
            st.info("🟢 Prediction: Low Risk of Diabetes")
