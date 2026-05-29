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

if "started" not in st.session_state:
    st.session_state.started = False

if "name" not in st.session_state:
    st.session_state.name = ""

if "quiz" not in st.session_state:
    from quiz import Quiz
    from data_manager import load_questions
    st.session_state.quiz = Quiz(load_questions())

import streamlit as st
from screens.welcome_screen import show_welcome
from screens.question_screen import show_question
from screens.results_screen import show_results

if not st.session_state.started:
    show_welcome()

elif st.session_state.quiz.has_more_questions():
    show_question()

else:
    show_results()



