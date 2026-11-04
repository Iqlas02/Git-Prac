import unittest
from password_reset import request_password_reset


class TestPasswordReset(unittest.TestCase):

    def test_empty_email(self):
        result = request_password_reset("")
        self.assertEqual(result, "Email is required")

    def test_valid_email(self):
        result = request_password_reset("user@example.com")
        self.assertEqual(result, "Password reset request received")


if __name__ == "__main__":
    unittest.main()