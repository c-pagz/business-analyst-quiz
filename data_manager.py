'''
This file handles all data operations for the Business Analyst Quiz.
It includes functions for loading questions from questions.csv and
saving quiz results to results.csv. These functions keep data
handling separate from the quiz logic and user interface, following
good coding practice.
'''

import csv
from question import Question


def load_questions():
    '''
    Loads quiz questions from the questions.csv file.

    This function:
    - Opens the CSV file containing all quiz questions
    - Skips the header row
    - Reads each question, its four answer options, and the correct answer
    - Creates a Question object for each row
    - Returns a list of Question objects for use in the quiz

    Returns:
        list: A list of Question instances created from the CSV data.
    '''
    questions = []

    with open("questions.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)  # Skip header row

        for row in reader:
            text = row[0]
            options = row[1:5]   # A, B, C, D
            correct = row[5]     # Correct answer letter

            q = Question(text, options, correct)
            questions.append(q)

    return questions


def save_result(name, score, total):
    '''
    Saves a user's quiz result to results.csv.

    This function:
    - Opens the results CSV file in append mode
    - Writes a new row containing the user's name, score, and total questions
    - Ensures results are stored persistently for later review or export

    Args:
        name (str): The user's name.
        score (int): The number of correct answers.
        total (int): The total number of quiz questions.
    '''
    with open("results.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, score, total])






