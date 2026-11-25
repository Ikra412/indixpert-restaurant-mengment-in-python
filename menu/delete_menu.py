
import json

def delete_menu():

    with open("data/menu.json", "r") as file:
        menu = json.load(file)

    print("\n----- DELETE MENU -----")

    for item in menu:
        print(item["id"], item["name"], item["price"])

    id = int(input("\nEnter Item ID to Delete: "))

    for item in menu:

        if item["id"] == id:

            menu.remove(item)

            with open("data/menu.json", "w") as file:
                json.dump(menu, file, indent=4)

            print("\nMenu Deleted Successfully!")
            return

    print("Item Not Found!")


if __name__ == "__main__":
    delete_menu()
