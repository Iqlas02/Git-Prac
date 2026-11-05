def get_notification_message(username):
    username = username.strip()

    if not username:
        return "Username is required"

    return f"Welcome, {username}! You have a new notification."