import streamlit as st

st.markdown(
    """
    <style>
    .stApp {
        background-color: #227B89;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def show_welcome():
    st.title("Welcome to the Business Analyst Quiz")
    st.subheader("10 questions to test your knowledge")

    st.session_state.name = st.text_input("Enter your name")

    if st.button("Start Quiz") and st.session_state.name != "":
        st.session_state.started = True
        st.rerun()

