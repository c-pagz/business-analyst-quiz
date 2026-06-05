import streamlit as st

# Apply background colour styling to match the design theme
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

    # Store the user's name in session state
    st.session_state.name = st.text_input("Enter your name")

    # Start the quiz only if a name has been entered
    if st.button("Start Quiz") and st.session_state.name != "":
        st.session_state.started = True
        st.rerun()

