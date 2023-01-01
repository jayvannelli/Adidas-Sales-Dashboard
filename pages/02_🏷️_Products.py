import streamlit as st
from src.data import df


def main():
    st.title("Product Breakdown")

    product = st.multiselect("Select product(s):",
                             options=df['Product'].unique(),
                             default=df['Product'].unique()[0])

    product_query = df.query("Product == @product")
    st.write(product_query)


if __name__ == "__main__":
    main()
