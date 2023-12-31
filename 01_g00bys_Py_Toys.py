import streamlit as st
from streamlit_extras.app_logo import add_logo

st.set_page_config(
    page_title="g00bys-Py-Toys!",
    page_icon="🐸",
    layout="wide",
    initial_sidebar_state="expanded"
)

add_logo("images/gbypyfrgy.png")

def main():
    st.title('g00bys Py Toys')
    st.write('Hello!\nI am g00by (aka Jakuu) and This is my streamlit! - More information to come!')

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
        background-color: #232428;
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
