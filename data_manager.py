import csv
from question import Question

# Load questions from questions.csv
def load_questions():
    questions = []

    with open("questions.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)  # skip header row

        for row in reader:
            text = row[0]
            options = row[1:5]   # A, B, C, D
            correct = row[5]     # correct answer letter

            q = Question(text, options, correct)
            questions.append(q)

    return questions


# Save results into results.csv
def save_result(name, score, total):
    with open("results.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, score, total])





