'''python
Controls the quiz flow by managing questions, tracking progress, and calculating scores.
The Quiz class acts as the main engine for the quiz logic.
'''

class Quiz:
    '''python
    Manages quiz state, including current question index and scoring.'''

    def __init__(self, questions):
        '''python
        Initialise the Quiz with a list of Question objects.

        Parameters:
            questions (list[Question]): The questions that make up the quiz.
        '''
        self.questions = questions
        self.current_index = 0
        self.score = 0

    def get_current_question(self):
        '''python
        Return the current question object.

        Returns:
            Question: The question at the current index.
        '''
        return self.questions[self.current_index]

    def submit_answer(self, user_answer):
        '''python
        Check the user's answer, update the score if correct,
        and move to the next question.

        Parameters:
            user_answer (str): The answer selected by the user.
        '''
        current_question = self.get_current_question()

        if current_question.is_correct(user_answer):
            self.score += 1

        self.current_index += 1

    def has_more_questions(self):
        '''python
        Check whether there are more questions left in the quiz.

        Returns:
            bool: True if more questions remain, otherwise False.
        '''
        return self.current_index < len(self.questions)

    def get_score(self):
        '''python
        Return the user's current score.

        Returns:
            int: Number of correct answers.
        '''
        return self.score

    def get_total_questions(self):
        '''python
        Return the total number of questions in the quiz.

        Returns:
            int: Total question count.
        '''
        return len(self.questions)

    def reset(self):
        '''python
        Reset the quiz back to the start.

        Sets the current question index and score back to zero.
        '''
        self.current_index = 0
        self.score = 0
