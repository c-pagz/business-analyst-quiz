"""
Defines the Question class, which represents a single multiple‑choice quiz question.
Each Question stores the text, four answer options, and the correct answer.
"""
class Question:
    
    """A single quiz question with text, options, and a correct answer."""
    def __init__(self, text, options, correct_answer):
        
        """
        Initialise a Question object.

        Parameters:
            text (str): The question text.
            options (list[str]): A list of possible answer options.
            correct_answer (str): The correct answer from the options list.
        """
        self.text = text
        self.options = options
        self.correct_answer = correct_answer
    
    def is_correct(self, user_answer):
        """
        Check whether the user's answer is correct.

        Parameters:
            user_answer (str): The answer selected by the user.

        Returns:
            bool: True if the answer matches the correct answer, otherwise False.
        """
        return user_answer == self.correct_answer