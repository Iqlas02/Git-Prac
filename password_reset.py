def request_password_reset(email):
    if not email:
        return "Email is required"

    return "Password reset request received"
