import streamlit as st
from src.data import get_adidas_sales_df

def display_kpis(data):
    """ """
    c1, c2, c3 = st.columns(3)
    with c1:
        st.subheader("Total Sales")
        st.write(f"${round(sum(data['Total Sales']), 2):,}")
    with c2:
        st.subheader("Operating Profit")
        st.write(f"${round(sum(data['Operating Profit']), 2):,}")
    with c3:
        st.subheader("Units Sold")
        st.write(f"{round(sum(data['Units Sold']), 2):,}")


st.title("Sales Overview")

df = get_adidas_sales_df()

display_kpis(df)
# st.write(df)

st.bar_chart(df, x="Region", y="Total Sales")
st.bar_chart(df, x="State", y="Total Sales")
st.bar_chart(df, x="City", y="Total Sales")
st.bar_chart(df, x="Invoice Date", y="Total Sales")