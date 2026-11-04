# Feature flag
PAYMENT_FEATURE_ENABLED = True


def payment_feature():
    if not PAYMENT_FEATURE_ENABLED:
        return "Payment feature is currently disabled"

    return "Payment feature is enabled"


# Execute the feature
print(payment_feature())