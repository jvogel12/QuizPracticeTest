from unittest import TestCase
import unittest
import QuizPractice

class TestAnswerChecker(TestCase):
    def test_check_answer_correct(self):
        #Arrange
        user_answer = "Chicago"
        correct_answer = "Chicago"
        #Act
        result = QuizPractice.check_answer(user_answer, correct_answer)
        #Assert
        self.assertTrue(result)

    def test_check_answer_is_correct_when_case_is_different(self):
        # Arrange
        user_answer = "chicago"
        correct_answer = "Chicago"

        # Act
        result = QuizPractice.check_answer(user_answer, correct_answer)

        # Assert
        self.assertTrue(result)

    def test_check_answer_is_correct_with_space_before_and_after(self):
        # Arrange
        user_answer = "    chicago    "
        correct_answer = "Chicago"

        # Act
        result = QuizPractice.check_answer(user_answer, correct_answer)

        # Assert
        self.assertTrue(result)

    def test_check_answer_is_incorrect_when_answers_are_different(self):
        # Arrange
        user_answer = "Boston"
        correct_answer = "Chicago"

        # Act
        result = QuizPractice.check_answer(user_answer, correct_answer)

        # Assert
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
