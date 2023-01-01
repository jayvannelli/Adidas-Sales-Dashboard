import streamlit as st
from src.data import get_adidas_sales_df

st.title("Adidas Sales Dashboard")

df = get_adidas_sales_df()
st.write(df)