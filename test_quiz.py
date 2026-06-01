'''
This file contains automated unit tests for the Quiz application.
The tests use Python's built‑in unittest framework to verify that
the quiz logic behaves correctly. These tests run independently
from the Streamlit interface and focus only on the underlying
functionality such as scoring, question progression, and reset
behaviour.
'''

import unittest
from quiz import Quiz
from question import Question


class TestQuiz(unittest.TestCase):
    '''
    This class contains a collection of unit tests for the Quiz class.
    Each test checks a specific behaviour of the quiz to ensure that
    the logic works correctly and consistently.
    '''

    def setUp(self):
        '''
        This method runs before every test.
        It creates two sample Question objects and a Quiz instance
        so each test starts with a fresh quiz in a known state.
        '''
        q1 = Question("Test Q1", ["A", "B", "C", "D"], "A")
        q2 = Question("Test Q2", ["A", "B", "C", "D"], "B")
        self.quiz = Quiz([q1, q2])

    def test_initial_state(self):
        '''
        Tests that the quiz starts correctly.
        The current question index should be 0 and the score should be 0.
        '''
        self.assertEqual(self.quiz.current_index, 0)
        self.assertEqual(self.quiz.score, 0)

    def test_correct_answer_increases_score(self):
        '''
        Tests that answering a question correctly increases the score by 1.
        '''
        self.quiz.answer_question("A")
        self.assertEqual(self.quiz.score, 1)

    def test_incorrect_answer_does_not_increase_score(self):
        '''
        Tests that answering incorrectly does not increase the score.
        '''
        self.quiz.answer_question("C")
        self.assertEqual(self.quiz.score, 0)

    def test_question_progression(self):
        '''
        Tests that after answering a question, the quiz moves to the next one.
        '''
        self.quiz.answer_question("A")
        self.assertEqual(self.quiz.current_index, 1)

    def test_reset_function(self):
        '''
        Tests that the reset method returns the quiz to its initial state.
        Score should return to 0 and the question index should reset to 0.
        '''
        self.quiz.answer_question("A")
        self.quiz.reset()
        self.assertEqual(self.quiz.score, 0)
        self.assertEqual(self.quiz.current_index, 0)


if __name__ == "__main__":
    '''
    This allows the test file to be run directly using:
    python3 -m unittest test_quiz.py
    '''
    unittest.main()
