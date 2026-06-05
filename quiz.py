class Quiz:

    def __init__(self, questions):

        self.questions = questions
        self.current_index = 0
        self.score = 0

    def get_current_question(self):
        return self.questions[self.current_index]

    def submit_answer(self, user_answer):
        current_question = self.get_current_question()

        if current_question.is_correct(user_answer):
            self.score += 1

        self.current_index += 1

    def has_more_questions(self):
        return self.current_index < len(self.questions)

    def get_score(self):
        return self.score

    def get_total_questions(self):
        return len(self.questions)

    def reset(self):
        self.current_index = 0
        self.score = 0
