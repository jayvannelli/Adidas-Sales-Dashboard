import streamlit as st
from src.data import df


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

    display_kpis(df)

    st.bar_chart(df, x="Region", y="Total Sales")

    st.write("---")

    st.subheader("Total Sales Demographics")
    st.bar_chart(df, x="State", y="Total Sales")
    st.bar_chart(df, x="City", y="Total Sales")

    st.subheader("Invoices Over Time")
    st.bar_chart(df, x="Invoice Date", y="Total Sales")


if __name__ == "__main__":
    main()
