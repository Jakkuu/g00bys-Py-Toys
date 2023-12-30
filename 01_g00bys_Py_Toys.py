import streamlit as st

st.set_page_config(
    page_title="g00bys-Py-Toys!",
    page_icon="🎢",
    layout="wide",
    initial_sidebar_state="expanded"
)


def main():
    st.title('Jakku Webspace In Progress!')
    st.write('Not quite sure what ill be doing yet, But here is my streamlit!')

    st.markdown("""
        <style>
        [data-testid=stButton] > button {
        background-color: #81A88D;
        color:#ffffff;
        }
        [data-testid=stAppViewContainer]{
        background-color: #81A88D;
        }
        [data-testid=stHeader]{
        background-color: #81A88D;
        }
        [data-testid=stSidebar] {
        background-color: #D3D4D8;
        }
        [data-testid=stButton] > button:hover {
        background-color: #A2A475;
        border-color:#ffffff;
        color:#ffffff;
        }
        [data-testid=stButton] > button:focus:not(:active) {
        background-color: #A2A475;
        border-color:#ffffff;
        color:#ffffff;
        }
        </style>""", unsafe_allow_html=True)


if __name__ == "__main__":
    main()
