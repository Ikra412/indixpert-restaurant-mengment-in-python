
import json

def update_menu():

    with open("data/menu.json", "r") as file:
        menu = json.load(file)

    print("\n----- UPDATE MENU -----")

    for item in menu:
        print(item["id"], item["name"], item["price"])

    id = int(input("\nEnter Item ID: "))

    for item in menu:

        if item["id"] == id:

            name = input("Enter New Food Name: ")
            price = float(input("Enter New Price: "))

            item["name"] = name
            item["price"] = price

            with open("data/menu.json", "w") as file:
                json.dump(menu, file, indent=4)

            print("\nMenu Updated Successfully!")
            return

    print("Item Not Found!")


if __name__ == "__main__":
    update_menu()
