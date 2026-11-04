def process_payment(amount):
    if not isinstance(amount, (int, float)):
        return "Invalid payment amount"

    if amount <= 0:
        return "Invalid payment amount"

    return "Payment processed successfully"