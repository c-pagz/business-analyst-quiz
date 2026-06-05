import streamlit as st

def show_question():

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

