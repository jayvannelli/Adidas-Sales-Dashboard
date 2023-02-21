import streamlit as st

from streamlit_extras.colored_header import colored_header
from src.data import get_adidas_sales_df


def main():
    st.title("Retailer Breakdown")

    df = get_adidas_sales_df()

    retailer = st.selectbox("Select retailer:", options=df['Retailer'].unique())
    retailer_df = df.loc[df['Retailer'] == retailer]

    colored_header(label=f"{retailer} Sales Analysis",
                   description="",
                   color_name="yellow-80")

    st.write("Sales by day of week")
    retailer_df['Invoice Date Name'] = retailer_df['Invoice Date'].dt.day_name()
    st.bar_chart(retailer_df, x="Invoice Date Name", y=["Total Sales", "Operating Profit"])

    st.write("Sales by method")
    st.bar_chart(retailer_df, x="Sales Method", y="Total Sales")

    st.write("Operating profit by product")
    st.bar_chart(retailer_df, x="Product", y="Operating Profit")

    st.write("Operating profit by state")
    st.bar_chart(retailer_df, x="State", y="Operating Profit")


if __name__ == "__main__":
    main()
