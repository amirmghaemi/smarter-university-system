from datetime import datetime
import unittest
import json

from app.controllers.quizzes_controller import QuizzesController

class QuizzesTest(unittest.TestCase):

    def setUp(self):
        # Run tests on non-production data
        self.ctrl = QuizzesController('quizzes_test.py')
        
    def test_expose_failure_01(self):
        """
        We load a JSON file that is empty

        json.decoder.JSONDecodeError: Expecting property name enclosed in double quotes
        """
        with self.assertRaises(json.decoder.JSONDecodeError):
            QuizzesController("bad_data.json")
         
    def test_expose_failure_02(self):
        '''
        Crash in QuizzesController.add_answer() when adding an answer to a non-existent question
        File: quizzes_controller.py, Line: 78
        '''       
        controller = QuizzesController()
        with self.assertRaises(AttributeError):
            controller.add_answer('non-existent-question-id', 'text', True)

    def test_expose_failure_03(self):
        """
        Testing the ability to add question to a non-existent-quiz-id
        """
        controller = QuizzesController()
        with self.assertRaises(AttributeError):
            controller.add_question('non-existent-quiz-id', 'title', 'text')

if __name__ == '__main__':
    unittest.main()
