import streamlit as st
from src.data import get_adidas_sales_df
from pycaret.regression import setup, compare_models, pull, save_model


df = get_adidas_sales_df()


def main():
    st.title("Find best Machine Learning Model with Pycaret")

    target_value = st.selectbox("Select target value", options=["Units Sold", "Operating Profit"])
    train_model = st.button("Train model")

    if train_model:
        setup(df, target=target_value)
        setup_df = pull()

        st.info("Machine Learning Experiment Settings")
        st.dataframe(setup_df)
        best_models = compare_models()
        compare_df = pull()

        st.info("Trained Machine Learning Model")
        st.dataframe(compare_df)


if __name__ == "__main__":
    main()
