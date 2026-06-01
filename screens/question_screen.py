'''
This file defines the question screen for the Business Analyst Quiz.
It displays one question at a time, shows all available answer options,
and handles the user's selection. When an option is clicked, the quiz
logic updates the score and moves to the next question.
'''

import streamlit as st

def show_question():
    '''
    Displays the current quiz question and its multiple‑choice options.

    This function:
    - Retrieves the active quiz instance from session state
    - Shows the current question number and total number of questions
    - Displays the question text
    - Creates a button for each answer option
    - Submits the selected answer and reloads the screen

    The screen automatically progresses to the next question after
    the user selects an option.
    '''
    quiz = st.session_state.quiz
    question = quiz.get_current_question()

    # Display question number and text
    st.header(f"Question {quiz.current_index + 1} of {quiz.get_total_questions()}")
    st.write(question.text)

    # Display answer options as buttons
    for option in question.options:
        if st.button(option):
            quiz.submit_answer(option)
            st.rerun()

