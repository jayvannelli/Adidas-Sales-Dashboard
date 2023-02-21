import streamlit as st
import datetime as dt

from streamlit_extras.colored_header import colored_header
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


def main():
    st.title("Sales Overview")

    colored_header(label="",
                   description="",
                   color_name="red-70")

    df = get_adidas_sales_df()
    display_kpis(df)

    st.bar_chart(df, x="Region", y="Total Sales")

    st.subheader("Quantity of Invoices Over Time")
    st.bar_chart(df, x="Invoice Date", y="Total Sales")

    st.write("---")

    colored_header(label="Total Sales Demographics",
                   description="Total sales broken down by day of the week, state & city.",
                   color_name="light-blue-70")

    df['Invoice Date Name'] = df['Invoice Date'].dt.day_name()
    st.bar_chart(df, x="Invoice Date Name", y="Total Sales")

    st.bar_chart(df, x="State", y="Total Sales")
    st.bar_chart(df, x="City", y="Total Sales")


if __name__ == "__main__":
    main()
