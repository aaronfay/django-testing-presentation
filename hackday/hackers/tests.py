from unittest import mock, TestCase

from hackers import registrar


class SignupTestCase(TestCase):
    # The Uncle Bob Way™

    def test_should_sign_up_user(self):
        # patch custom save method
        with mock.patch('hackers.registrar.save_participant') as mock_save:
            # call registrar.add_participant
            registrar.add_participant('foo@bar.com')
            # assert called
            self.assertTrue(mock_save.called)




























        # with mock.patch('hackers.registrar.save_participant') as mock_save:
        #     registrar.add_participant('foo')
        #     self.assertTrue(mock_save.called)