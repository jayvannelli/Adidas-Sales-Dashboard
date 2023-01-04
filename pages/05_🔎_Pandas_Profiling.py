import streamlit as st
import pandas_profiling

from src.data import get_adidas_sales_df
from streamlit_pandas_profiling import st_profile_report


def main():
    st.title("Adidas Sales Profile Report")

    df = get_adidas_sales_df()

    generate_button = st.button("Generate report")
    if generate_button:
        profile_report = df.profile_report()
        st_profile_report(profile_report)


if __name__ == "__main__":
    main()
