import streamlit as st
from src.data import get_adidas_sales_df

df = get_adidas_sales_df()

product = st.multiselect("Select product(s):",
                         options=df['Product'].unique(),
                         default=df['Product'].unique()[0])

product_query = df.query("Product == @product")
st.write(product_query)