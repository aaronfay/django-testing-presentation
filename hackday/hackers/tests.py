from django.test import TestCase
from django.test import Client

from hackers.models import Participant


class SignupTestCase(TestCase):
    # The Django Way™

    def setUp(self):
        self.client = Client()

    def test_should_sign_up_user(self):
        expected_email = 'joe@python.com'
        # post the data in
        # query the db model
        # assert the model you got back matches

























        # self.client.post('/', {'email': expected_email})
        # test = Participant.objects.get(email=expected_email)
        # self.assertEqual(test.email, expected_email)
