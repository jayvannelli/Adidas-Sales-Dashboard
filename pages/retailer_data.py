import streamlit as st
from src.data import get_adidas_sales_df

df = get_adidas_sales_df()

retailer = st.selectbox("Select retailer:", options=df['Retailer'].unique())

retailer_df = df.loc[df['Retailer'] == retailer]

st.subheader(f"{retailer} Total Sales by Method")
st.bar_chart(retailer_df, x="Sales Method", y="Total Sales")

st.subheader(f"{retailer} Operating Profit by Product")
st.bar_chart(retailer_df, x="Product", y="Operating Profit")

st.subheader(f"{retailer} Operating Profit by State")
st.bar_chart(retailer_df, x="State", y="Operating Profit")
