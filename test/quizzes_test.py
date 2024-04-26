from datetime import datetime
import unittest

from app.controllers.quizzes_controller import QuizzesController

class QuizzesTest(unittest.TestCase):

    def setUp(self):
        # Run tests on non-production data
        self.ctrl = QuizzesController('quizzes_test.py')
        
 def test_expose_failure_01(self):
        """
        We load a JSON file that is empty

        The error occurs in the app/utils/data_loader.py, line 13 when loading the data:
            return json.load(fin)

        json.decoder.JSONDecodeError: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
        """
        _ = QuizzesController("bad_data.json")
        assert _ is QuizzesController
         self.assertIsNone(newly_added_question, "Test should fail as no data exists in the JSON")

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
        Testing the ability to create a quiz with a NoneType data and causing a crash
        """
        test_available_date = datetime(2024, 4, 23, 12, 0, 0)
        test_due_date = datetime(2024, 4, 24, 12, 0, 0)
        test_quiz_id = self.ctrl.add_quiz(None, 'test', test_available_date, test_due_date)
        test_quiz = self.ctrl.get_quiz_by_id(test_quiz_id)
        self.assertIsNotNone(test_quiz, 'Get None quiz.')

        '''
        crash info:
        File "smarter-university-system/./app/controllers/quizzes_controller.py", line 63, in add_quiz
            quiz_id = utils.generate_id(title + updated_date.isoformat())
        TypeError: unsupported operand type(s) for +: 'NoneType' and 'str'
        '''



if __name__ == '__main__':
    unittest.main()
