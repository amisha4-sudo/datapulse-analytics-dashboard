import streamlit as st
import pandas as pd

st.title("📊 DataPulse Dashboard")

data = pd.DataFrame({
    "Sales": [100, 200, 150, 300],
    "Month": ["Jan", "Feb", "Mar", "Apr"]
})

st.bar_chart(data.set_index("Month"))
