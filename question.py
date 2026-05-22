class Question:
    def __init__(self, text, options, correct_answer):
        self.text = text
        self.options = options
        self.correct_answer = correct_answer
    
    def is_correct(self, user_answer):
        return user_answer == self.correct_answer