'''python
Streamlit interface for the Business Analyst Quiz application.

This file controls:
- The welcome screen
- Starting the quiz
- Displaying questions one at a time
- Handling user input
- Shogit wing the final score and personalised feedback
- Saving results to CSV
- Restarting the quiz

The logic is kept simple and beginner‑friendly, while the Quiz and Question
classes handle the core functionality.
''' 

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from quiz import Quiz
from data_manager import load_questions, save_result

# Set background colour
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

# Load questions once
questions = load_questions()

# Set up session state
if "quiz" not in st.session_state:
    st.session_state.quiz = Quiz(questions)

if "name" not in st.session_state:
    st.session_state.name = ""

if "started" not in st.session_state:
    st.session_state.started = False

quiz = st.session_state.quiz

# Welcome Screen
if not st.session_state.started:
    st.title("Welcome to the Business Analyst Quiz")
    st.subheader("10 questions to test your knowledge")

    st.session_state.name = st.text_input("Enter your name")

    if st.button("Start Quiz") and st.session_state.name != "":
        st.session_state.started = True
        st.rerun()

# Question Screen
elif quiz.has_more_questions():
    question = quiz.get_current_question()

    st.header(f"Question {quiz.current_index + 1} of {quiz.get_total_questions()}")
    st.write(question.text)

    for option in question.options:
        if st.button(option):
            quiz.submit_answer(option)
            st.rerun()

# Results Screen
else:
    score = quiz.get_score()
    total = quiz.get_total_questions()

    # Score‑based personalised message
    if score >= 7:
        st.success(f"Excellent work, {st.session_state.name}!")
    elif 5 <= score < 7:
        st.info(f"Good work, {st.session_state.name}!")
    else:
        st.warning(f"Practice makes perfect, {st.session_state.name}!")

    st.write(f"Your score: **{score}/{total}**")

    # Pie chart data
    correct = score
    incorrect = total - score

    df = pd.DataFrame({
        "Result": ["Correct", "Incorrect"],
        "Count": [correct, incorrect]
    })

    # Create pie chart with green/red colours
    fig, ax = plt.subplots()
    ax.pie(
        df["Count"],
        labels=df["Result"],
        autopct="%1.1f%%",
        colors=["green", "red"]
    )
    ax.axis("equal")

    st.subheader("Your Results")
    st.pyplot(fig)

    # Save result
    save_result(st.session_state.name, score, total)

    # Download results
    csv_data = f"name,score,total\n{st.session_state.name},{score},{total}"
    st.download_button("Download Results", csv_data, "results.csv")

    # Restart quiz
    if st.button("Restart Quiz"):
        st.session_state.quiz = Quiz(questions)
        st.session_state.name = ""
        st.session_state.started = False
        st.rerun()


