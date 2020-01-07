import unittest

from survey import AnonymousSurvey

class TestAnonmyousSurvey(unittest.TestCase):

    def setUp(self):
        question = "What language did you first learn to speak?"
        self.survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        response = self.responses[0]
        self.survey.store_response(response)
        self.assertIn(response, self.survey.responses)

    def test_store_three_responses(self):
        responses = ['English', 'Spanish', 'Mandarin']
        for response in self.responses:
            self.survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.survey.responses)