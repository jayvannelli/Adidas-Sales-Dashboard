import streamlit as st


def main():
    st.title("Adidas United States Sales | Kaggle Dataset")

    left_column, _, right_column = st.columns([3, 1, 3])
    with left_column:
        st.write("")
        st.image("images/streamlit-logo-secondary-lightmark-lighttext.png")
        st.image("images/kaggle.png")
    with right_column:
        st.image("images/adidas.jpeg")


if __name__ == "__main__":
    main()
