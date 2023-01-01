import streamlit as st
import pandas as pd

ADIDAS_SALES_FILEPATH: str = "data/Adidas_US_Sales_Datasets.xlsx"


@st.cache(allow_output_mutation=True)
def get_adidas_sales_df() -> pd.DataFrame:
    """Returns Adidas Sales csv file as pandas DataFrame."""
    raw_df = pd.read_excel(ADIDAS_SALES_FILEPATH, skiprows=4)
    return raw_df.drop(columns="Unnamed: 0")
