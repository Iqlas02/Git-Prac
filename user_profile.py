def get_user_profile(name, email):
    return {
        "name": name,
        "email": email
    }


profile = get_user_profile("Iqlas", "iqlas@example.com")

print(profile)