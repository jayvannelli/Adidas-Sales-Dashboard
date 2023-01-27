import streamlit as st
from src.data import get_adidas_sales_df


def main():
    st.title("Query Dataset")

    df = get_adidas_sales_df()

    product = st.multiselect("Select product(s):",
                             options=df['Product'].unique(),
                             default=df['Product'].unique()[0])

    state = st.multiselect("Select state(s):",
                           options=df['State'].unique(),
                           default=df['State'].unique()[0])

    retailer = st.multiselect("Select retailer(s):",
                              options=df['Retailer'].unique(),
                              default=df['Retailer'].unique()[0])

    product_query = df.query(
        "Product == @product & State == @state & Retailer == @retailer"
    )

    st.write("---")

    if len(product_query) > 1:
        c1, c2, c3 = st.columns(3)
        with c1:
            st.subheader("Total Sales")
            st.write(f"Total Sales: ${round(sum(product_query['Total Sales']), 2):,}")
        with c2:
            st.subheader("Operating Profit")
            st.write(f"Operating Profit: ${round(sum(product_query['Operating Profit']), 2):,}")
        with c3:
            st.subheader("Total Orders")
            st.write(len(product_query))

        st.write("---")

        st.bar_chart(product_query, x="Retailer", y="Total Sales")
        st.bar_chart(product_query, x="City", y="Operating Profit")
    else:
        st.info("Please select products.")


if __name__ == "__main__":
    main()
