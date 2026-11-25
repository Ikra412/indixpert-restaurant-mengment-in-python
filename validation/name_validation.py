
def validate_name(name):

    if name == "":
        print("Name cannot be empty!")
        return False

    if not name.replace(" ", "").isalpha():
        print("Name should contain only letters!")
        return False

    return True
