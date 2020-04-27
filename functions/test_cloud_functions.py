import unittest
from .main import (create_message, create_profile, create_user)
from unittest.mock import Mock


class CreateMessageTests(unittest.TestCase):
    def setUp(self):
        # Declare test data variables here
        self.expected_fail_string = 'Failure: invalid payload'
        self.bad_data = '{"malformed payload": some junk}'
        self.ok_JSON = {"messagePayload":
                        {"messageContent": "Kilroy was here",
                         "category": "test", "urgency": "99",
                         "resourceURL": "http://endless.horse/",
                         "tags": ["thing", "thang", "thunk"]}}
        self.on_add_string = "Message added"

    def test_receiving_json(self):
        """ tests the ablility to receive messagePayload in JSON form
        create mock variable"""
        req = Mock(get_json=Mock(return_value=self.ok_JSON),
                   args=self.ok_JSON)
        assert self.on_add_string in create_message(req) and \
            "POST" in create_message(req)

    def test_receiving_args(self):
        """tests the ablility to receive messagePayload in NON-JSON form
        create mock variable"""
        req = Mock(get_json=Mock(return_value=None),
                   args=self.ok_JSON)
        assert self.on_add_string in create_message(req) and \
            "GET" in create_message(req)

    def test_bad_payload(self):
        """ confirms that function errors on malformed payload """
        req = Mock(get_json=Mock(return_value=self.bad_data),
                   args=self.bad_data)
        assert create_message(req) == self.expected_fail_string


class CreateProfileTests(unittest.TestCase):
    def setUp(self):
        # Declare test data variables here
        self.expected_fail_string = 'Failure: invalid payload'
        self.bad_data = '{"malformed payload": some junk}'
        self.ok_JSON = {"profilePayload":
                        {"userID": "777", "receiveSMSflag": "0",
                         "receivePushFlag": "1", "messageFrequency": "1",
                         "isProfileActive": "1", "preferredTags":
                            ["foo", "bar", "baz"]}}
        self.on_add_string = "Profile added"

    def test_receiving_json(self):
        """ tests the ablility to receive messagePayload in JSON form
        create mock variable"""
        req = Mock(get_json=Mock(return_value=self.ok_JSON),
                   args=self.ok_JSON)
        assert self.on_add_string in create_profile(req) and \
            "POST" in create_profile(req)

    def test_receiving_args(self):
        """tests the ablility to receive messagePayload in NON-JSON form
        create mock variable"""
        req = Mock(get_json=Mock(return_value=None),
                   args=self.ok_JSON)
        assert self.on_add_string in create_profile(req) and \
            "GET" in create_profile(req)

    def test_bad_payload(self):
        """ confirms that function errors on malformed payload """
        req = Mock(get_json=Mock(return_value=self.bad_data),
                   args=self.bad_data)
        assert create_profile(req) == self.expected_fail_string


class CreateUserTest(unittest.TestCase):
    def setUp(self):
        # Declare test data variables here
        self.expected_fail_string = 'Failure: invalid payload'
        self.bad_data = '{"malformed payload": some junk}'
        self.ok_JSON = {"userPayload":
                        {"userID": "c2AgcDSh0fe:APA91bHu02",
                         "userName": "Drewsuf Islam",
                         "phoneNum": "8675309",
                         "profiles": ["profileID1", "profileID2"]}}
        print(self.ok_JSON)
        self.on_add_string = "User added"

    def test_receiving_json(self):
        """ tests the ablility to receive messagePayload in JSON form
        create mock variable"""
        req = Mock(get_json=Mock(return_value=self.ok_JSON),
                   args=self.ok_JSON)
        assert self.on_add_string in create_user(req) and \
            "POST" in create_user(req)

    def test_receiving_args(self):
        """tests the ablility to receive messagePayload in NON-JSON form
        create mock variable"""
        req = Mock(get_json=Mock(return_value=None),
                   args=self.ok_JSON)
        assert self.on_add_string in create_user(req) and \
            "GET" in create_user(req)

    def test_bad_payload(self):
        """ confirms that function errors on malformed payload """
        req = Mock(get_json=Mock(return_value=self.bad_data),
                   args=self.bad_data)
        assert create_user(req) == self.expected_fail_string


class SampleTests(unittest.TestCase):
    """
    Dummy tests developed to characterize the test frameworks capabilities
    preserved as a reference
    """
    def setUp(self):
        """ create data variables here. setUp is called at the start of the run
        by the test harness, so these can be used anywhere in class
        """
        self.expected_int = 5
        self.expected_string = "This is a test message"

    def test_calculates_then_tests_results(self):
        """
        tests the sum function behaves as expected. sub a function we created
        """
        actual_int = sum([3, 2])
        self.assertEqual(self.expected_int, actual_int)

    def test_behavior_that_errors(self):
        """ tests the assertRaisesRegex tooling"""
        with self.assertRaisesRegex(ZeroDivisionError, "division by zero"):
            self.div_z(self.expected_int)

    def div_z(self, some_number):
        """ a helper function for test_behavior_that_error"""
        return some_number / 0
