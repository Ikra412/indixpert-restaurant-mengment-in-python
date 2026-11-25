
def validate_password(password):

    if len(password) < 8:
        print("Password must be at least 8 characters!")
        return False

    if not any(char.isupper() for char in password):
        print("Password must contain one uppercase letter!")
        return False

    if not any(char.islower() for char in password):
        print("Password must contain one lowercase letter!")
        return False

    if not any(char.isdigit() for char in password):
        print("Password must contain one number!")
        return False

    return True
