import streamlit as st
from src.data import get_adidas_sales_df


def main():
    st.title("State Breakdown")

    df = get_adidas_sales_df()

    state = st.selectbox("Select state:", options=df['State'].unique())

    state_df = df.loc[df['State'] == state]

    st.subheader("Units Sold (by retailer)")
    st.bar_chart(state_df, x="Retailer", y="Units Sold")

    st.subheader("Sales Method")
    st.bar_chart(state_df, x="Sales Method", y="Units Sold")

    st.subheader(f"Units Sold and Operating Profit (by product)")
    left_col, right_col = st.columns(2)
    with left_col:
        st.bar_chart(state_df, x="Product", y="Units Sold")
    with right_col:
        st.bar_chart(state_df, x="Product", y="Operating Profit")

    # st.write(df)


if __name__ == "__main__":
    main()
