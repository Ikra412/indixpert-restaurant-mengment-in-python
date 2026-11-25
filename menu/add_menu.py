
import json


def add_menu():

    print("\n")
    print("=" * 45)
    print("          ADD NEW MENU ITEM")
    print("=" * 45)

    with open("data/menu.json", "r") as file:
        menu = json.load(file)

    name = input("\nEnter Food Name: ")

    try:
        price = float(input("Enter Food Price: "))
    except ValueError:
        print("\nPlease Enter a Valid Price!")
        return False

    if price <= 0:
        print("\nPrice Must Be Greater Than Zero!")
        return False

    item_id = max((item["id"] for item in menu), default=0) + 1

    new_item = {
        "id": item_id,
        "name": name,
        "price": price
    }

    menu.append(new_item)

    with open("data/menu.json", "w") as file:
        json.dump(menu, file, indent=4)

    print("\nMenu Item Added Successfully!")
    print("=" * 45)

    return True


if __name__ == "__main__":
    add_menu()
