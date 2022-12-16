import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np

text = "I am trying my first store"

st.title("Maha Bridal Studio")
st.write(text)
df = sns.load_dataset("iris")
df = df.head()
df
chart_data = pd.DataFrame(
    np.random.randn(50, 2),
    columns=["sepal_length", "sepal_width"])

st.bar_chart(chart_data)