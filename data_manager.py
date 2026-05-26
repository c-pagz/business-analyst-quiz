"""
Handles loading quiz questions from a CSV file and saving user results.
This module separates data handling from quiz logic for cleaner design.
"""

from question import Question
import csv

def load_questions():
    """
    Load questions from 'questions.csv' and return them as Question objects.

    Returns:
        list[Question]: A list of Question instances created from the CSV data.

    Raises:
        FileNotFoundError: If the CSV file is missing.
        ValueError: If required fields are missing or incorrectly formatted.
    """
    questions = []
    with open("questions.csv", "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  # skip header

        for row in reader:
            text = row[0]
            options = row[1:5]
            correct_answer = row[5]

            q = Question(text, options, correct_answer)
            questions.append(q)

    return questions


def save_result(name, score, total):
    """
    Append the user's quiz result to 'results.csv'.

    Parameters:
        name (str): The user's name.
        score (int): Number of correct answers.
        total (int): Total number of questions.
    """
    with open("results.csv", "a", encoding="utf-8") as file:
        file.write(f"{name},{score},{total}\n")


