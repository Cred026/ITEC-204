import unittest
from enum import Enum

# Mocking your type_map and QuestionType for testing
class QuestionType(Enum):
    MULTIPLE_CHOICE = "multiple_choice"
    ESSAY = "essay"

type_map = {
    "multiple_choice": QuestionType.MULTIPLE_CHOICE,
    "essay": QuestionType.ESSAY
}

# Function under test
def handle_survey_input_exists(svy_questions: dict) -> tuple[bool, list]:
    qflag = []
    each_qcheck = []

    for qcounter, (qkey, qvalue) in enumerate(svy_questions.items(), start=1):
        result = {}
        each_qdata = []
        q_type = type_map.get(qvalue.get("type", "").lower(), "")

        if not qkey:
            result[f"Question{qcounter}"] = False
            each_qdata.append(True)

        if not qvalue.get("questionNum"):
            result["questionNum"] = False
            each_qdata.append(True)

        if not qvalue.get("type"):
            result["type"]= False
            each_qdata.append(True)

        if q_type == QuestionType.MULTIPLE_CHOICE:
            if not qvalue.get("choice"):
                result["choice"] = False
                each_qdata.append(True)

        if not qvalue.get("answer"):
            result["answer"] = False
            each_qdata.append(True)

        if result:
            qflag.append({f"Question {qcounter}": result})

        each_qcheck.append(any(each_qdata))
        qcounter +=1

    return any(each_qcheck), qflag

# Unit Test
class TestHandleSurveyInputExists(unittest.TestCase):

    def test_all_correct(self):
        questions = {
            "Q1": {"questionNum": 1, "type": "essay", "answer": "Some answer"},
            "Q2": {"questionNum": 2, "type": "multiple_choice", "choice": ["A","B"], "answer": "A"}
        }
        flag, messages = handle_survey_input_exists(questions)
        self.assertFalse(flag)
        self.assertEqual(messages, [])

    def test_missing_fields(self):
        questions = {
            "": {"questionNum": 1, "type": "essay", "answer": "Some answer"},
            "Q2": {"questionNum": None, "type": "", "answer": ""}
        }
        flag, messages = handle_survey_input_exists(questions)
        self.assertTrue(flag)
        self.assertEqual(len(messages), 2)
        self.assertIn("Question 1", messages[0])
        self.assertIn("Question 2", messages[1])

    def test_missing_choice_multiple_choice(self):
        questions = {
            "Q1": {"questionNum": 1, "type": "multiple_choice", "choice": [], "answer": "A"}
        }
        flag, messages = handle_survey_input_exists(questions)
        self.assertTrue(flag)
        self.assertIn("choice", messages[0]["Question 1"])

if __name__ == "__main__":
    unittest.main()
