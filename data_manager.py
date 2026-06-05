import csv
from question import Question


def load_questions():
    questions = []

    with open("questions.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)

        for row in reader:
            text = row[0]
            options = row[1:5]   
            correct = row[5]     

            q = Question(text, options, correct)
            questions.append(q)

    return questions


def save_result(name, score, total):
    with open("results.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, score, total])






