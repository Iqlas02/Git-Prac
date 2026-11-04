def get_user_profile(name, email):
    if not name:
        raise ValueError("Name cannot be empty")

    if not email:
        raise ValueError("Email cannot be empty")

    return {
        "name": name,
        "email": email
    }


profile = get_user_profile("Iqlas", "iqlas@example.com")

print(profile)