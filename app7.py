import streamlit as st
import joblib
import pandas as pd
import numpy as np

model=joblib.load("model.pkl")
expected_columns=joblib.load("columns.pkl")

st.title("💎 Diamond Price Prediction")
st.write("Predict the price of a diamond using Machine Learning.")

st.markdown("---")

carat = st.number_input("Carat", 0.10, 6.00, 0.50)
cut = st.selectbox("Cut", ["Fair","Good","Very Good","Premium","Ideal"])
color = st.selectbox("Color", ["D","E","F","G","H","I","J"])
clarity = st.selectbox("Clarity", ["I1","SI2","SI1","VS2","VS1","VVS2","VVS1","IF"])
depth = st.number_input("Depth", 40.0, 80.0, 60.0)
table = st.number_input("Table", 40.0, 80.0, 55.0)
x = st.number_input("Length (x)", 0.0, 11.0, 5.00)
y = st.number_input("Width (y)", 0.0, 60.0, 5.00)
z = st.number_input("Height (z)", 0.0, 35.0, 3.10)

st.markdown("---")

if st.button("Predict Price"):

    raw_input = {
        'carat': carat,
        'depth': depth,
        'table': table,
        'x': x,
        'y': y,
        'z': z,
        'cut_' + cut: 1,
        'color_' + color: 1,
        'clarity_' + clarity: 1
    }

    input_df = pd.DataFrame([raw_input])

    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    input_df = input_df[expected_columns]

    prediction = model.predict(input_df)[0]

    st.write(f"Predicted Diamond Price: $",prediction)
