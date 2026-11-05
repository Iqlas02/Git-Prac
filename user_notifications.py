def get_notification_message(username):
    if not username:
        return "Username is required"

    return f"Welcome, {username}! You have a new notification."