import unittest
from quiz import Quiz
from question import Question


class TestQuiz(unittest.TestCase):
    

    def setUp(self):
        
        q1 = Question("Test Q1", ["A", "B", "C", "D"], "A")
        q2 = Question("Test Q2", ["A", "B", "C", "D"], "B")
        self.quiz = Quiz([q1, q2])

    def test_initial_state(self):
        self.assertEqual(self.quiz.current_index, 0)
        self.assertEqual(self.quiz.score, 0)

    def test_correct_answer_increases_score(self):       
        self.quiz.answer_question("A")
        self.assertEqual(self.quiz.score, 1)

    def test_incorrect_answer_does_not_increase_score(self):      
        self.quiz.answer_question("C")
        self.assertEqual(self.quiz.score, 0)

    def test_question_progression(self):
        self.quiz.answer_question("A")
        self.assertEqual(self.quiz.current_index, 1)

    def test_reset_function(self):
        self.quiz.answer_question("A")
        self.quiz.reset()
        self.assertEqual(self.quiz.score, 0)
        self.assertEqual(self.quiz.current_index, 0)


if __name__ == "__main__":
    unittest.main()
