import unittest
from .main import (create_message, create_profile, create_user)
# import unittest.mock as mock


class CreateMessageTests(unittest.TestCase):
    def setUp(self):
        # Declare test data variables here
        self.expected_int = 5
        self.expected_string = "This is a test message"

    def test_receiving_json(self):
        # tests the ablility to receive messagePayload in JSON form
        # create mock variable
        pass

    def test_receiving_args(self):
        # tests the ablility to receive messagePayload in NON-JSON form
        # create mock variable
        pass

    def test_bad_payload(self):
        # tests the ablility to receive messagePayload in NON-JSON form
        # create mock variable
        pass

# #################### dummy tests ###################################

    def test_calculates_then_tests_results(self):
        # tests the sum function behaves as expected.
        # In real life, this would be a function we declared
        actual_int = sum([3, 2])
        self.assertEqual(self.expected_int, actual_int)

    def test_behavior_that_errors(self):
        with self.assertRaisesRegex(ZeroDivisionError, "division by zero"):
            self.div_z(self.expected_int)

    def div_z(self, some_number):
        return some_number / 0

if __name__ == '__main__':
    unittest.main()
