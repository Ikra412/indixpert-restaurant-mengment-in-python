
import json
from validation.name_validation import validate_name
from validation.password_validation import validate_password


def staff_login():

    print("\n")
    print("=" * 45)
    print("       🍽️ RESTAURANT MANAGEMENT SYSTEM")
    print("=" * 45)
    print("                 STAFF LOGIN")
    print("-" * 45)

    with open("data/users.json", "r") as file:
        users = json.load(file)

    username = input("\n  enter Username : ")
    password = input("  enter Password : ")

    if not validate_name(username):
        return False

    if not validate_password(password):
        return False

    print("\n" + "-" * 45)

    for user in users:

        if (user["username"] == username and
            user["password"] == password and
            user["role"] == "staff"):

            print("\n  Welcome Staff!")
            print("  Login Successfully!")
            print("\n" + "=" * 45)

            return True

    print("\n  Invalid Username or Password!")
    print("  please try again.")
    print("\n" + "=" * 45)

    return False


if __name__ == "__main__":
    staff_login()
