from question import Question

def load_questions():
    questions = []

    with open("questions.csv", "r", encoding="utf-8") as file:
        lines = file.readlines()

        for line in lines[1:]:  # skip header
            parts = line.strip().split(",")

            text = parts[0].strip('"')
            option_a = parts[1].strip('"')
            option_b = parts[2].strip('"')
            option_c = parts[3].strip('"')
            option_d = parts[4].strip('"')
            correct_answer = parts[5].strip('"')

            options = [option_a, option_b, option_c, option_d]

            q = Question(text, options, correct_answer)
            questions.append(q)

    return questions


def save_result(name, score, total):
    with open("results.csv", "a", encoding="utf-8") as file:
        file.write(f"{name},{score},{total}\n")

