import unittest
import feature_flags


class TestPaymentFeature(unittest.TestCase):

    def test_payment_feature_disabled(self):
        feature_flags.PAYMENT_FEATURE_ENABLED = False

        result = feature_flags.payment_feature()

        self.assertEqual(
            result,
            "Payment feature is currently disabled"
        )

    def test_payment_feature_enabled(self):
        feature_flags.PAYMENT_FEATURE_ENABLED = True

        result = feature_flags.payment_feature()

        self.assertEqual(
            result,
            "Payment feature is enabled"
        )


if __name__ == "__main__":
    unittest.main()