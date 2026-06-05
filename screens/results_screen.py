import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from data_manager import save_result


def show_results():
    
    # Apply background colour styling
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

    quiz = st.session_state.quiz
    score = quiz.get_score()
    total_questions = quiz.get_total_questions()

    # Save the result to the CSV file
    save_result(st.session_state.name, score, total_questions)

    # Load the CSV and get the most recent result
    df = pd.read_csv("results.csv")
    last = df.iloc[-1]

    correct = int(last["score"])
    total = int(last["total"])
    incorrect = total - correct

    # Display personalised score message
    name = st.session_state.name

    if correct <= 4:
        st.subheader(f"Practice makes perfect, {name}!")
    elif 5 <= correct <= 7:
        st.subheader(f"Good work, {name}!")
    else:
        st.subheader(f"Excellent job, {name}!")

    # Create a pie chart showing correct vs incorrect answers
    fig, ax = plt.subplots()
    ax.pie(
        [correct, incorrect],
        labels=["Correct", "Incorrect"],
        autopct="%1.1f%%",
        colors=["green", "red"]
    )
    ax.axis("equal")  # Ensures the pie chart is circular

    st.pyplot(fig)

    # Button to download the full results CSV
    st.download_button(
        label="Download All Results (CSV)",
        data=df.to_csv(index=False),
        file_name="results.csv",
        mime="text/csv"
    )

    # Restart the quiz
    if st.button("Restart Quiz"):
        quiz.reset()
        st.session_state.started = False
        st.rerun()




