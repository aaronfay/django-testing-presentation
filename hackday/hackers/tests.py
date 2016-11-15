from django.test import TestCase
from django.test import Client

from hackers.models import Participant


class SignupTestCase(TestCase):
    # The Django Way™

    def setUp(self):
        self.client = Client()

    def test_should_sign_up_user(self):
        expected_email = 'jill@python.com'
        # post the data in
        self.client.post('/', {'email': expected_email})
        # query the db model
        test = Participant.objects.get(email=expected_email)

        # assert the model you got back matches
        self.assertEquals(expected_email, test.email)
