
import json

def update_order():

    with open("data/orders.json", "r") as file:
        orders = json.load(file)

    print("\n----- UPDATE ORDER -----")

    order_id = int(input("Enter Order ID: "))

    for order in orders:

        if order["id"] == order_id:

            print("\nCurrent Food:", order["food_name"])
            print("Current Quantity:", order["quantity"])
            print("Current Total:", order["total"])

            new_quantity = int(input("\nEnter New Quantity: "))

            with open("data/menu.json", "r") as file:
                menu = json.load(file)

            for item in menu:

                if item["name"].lower() == order["food_name"].lower():

                    order["quantity"] = new_quantity
                    order["total"] = item["price"] * new_quantity

                    break

            with open("data/orders.json", "w") as file:
                json.dump(orders, file, indent=4)

            print("\nOrder Updated Successfully!")
            break

    else:
        print("\nOrder Not Found!")


if __name__ == "__main__":
    update_order()
