import mock
import unittest

from hackers.forms import SignupForm
from hackers.models import Participant
from hackers.views import signup


class SignupTestCase(unittest.TestCase):
    # The Mocking Way™

    def setUp(self):
        self.email = 'jill@python.com'
        self.form = SignupForm(email=self.email)
        self.request = mock.Mock(method='POST', POST=)

    def test_should_sign_up_user(self):
        
        # post the data in
        # query the db model
        # assert the model you got back matches
