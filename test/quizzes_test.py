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
        

if __name__ == '__main__':
    unittest.main()
