'''
This file defines the welcome screen for the Business Analyst Quiz.
It handles the initial user interaction, including entering a name
and starting the quiz. The screen uses Streamlit components and
applies the project’s consistent background colour.
'''

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
    '''
    Displays the welcome screen of the quiz.
    This includes:
    - The quiz title and subtitle
    - A text input for the user to enter their name
    - A button to start the quiz once a name has been entered

    When the user clicks "Start Quiz" and a name is provided,
    the session state is updated and the app moves to the first question.
    '''
    st.title("Welcome to the Business Analyst Quiz")
    st.subheader("10 questions to test your knowledge")

    # Store the user's name in session state
    st.session_state.name = st.text_input("Enter your name")

    # Start the quiz only if a name has been entered
    if st.button("Start Quiz") and st.session_state.name != "":
        st.session_state.started = True
        st.rerun()

