from question import Question
import csv

def load_questions():
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
    with open("results.csv", "a", encoding="utf-8") as file:
        file.write(f"{name},{score},{total}\n")


