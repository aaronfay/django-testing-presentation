import unittest
from unittest import mock

from hackers.views import signup


class SignupTestCase(unittest.TestCase):
    # The Mocking Way™

    def setUp(self):
        self.email = 'jill@python.com'
        self.request = mock.Mock(method='POST',
                                 POST={'email': self.email})

    def test_should_sign_up_user(self):
        # patch the model.save method
        with mock.patch('hackers.models.Participant.save') as mock_save:
            # call the signup view
            signup(self.request)
            # assert saved
            self.assertTrue(mock_save.called)
