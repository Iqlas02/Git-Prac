import unittest
from user_notifications import get_notification_message


class TestNotifications(unittest.TestCase):
    def test_username_with_whitespace(self):
     result = get_notification_message(" Iqlas ")
     self.assertEqual(
        result,
        "Welcome, Iqlas! You have a new notification."
    )

    def test_valid_username(self):
        result = get_notification_message("Iqlas")
        self.assertEqual(
            result,
            "Welcome, Iqlas"
        )

    def test_empty_username(self):
        result = get_notification_message("")
        self.assertEqual(result, "Username is required")


if __name__ == "__main__":
    unittest.main()