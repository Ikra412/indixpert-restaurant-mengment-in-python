
import json
from datetime import datetime

def new_order():

    with open("data/orders.json", "r") as file:
        orders = json.load(file)

    print("\n----- NEW ORDER -----")

    customer_name = input("Enter Customer Name: ")
    food_name = input("Enter Food Name: ")
    quantity = int(input("Enter Quantity: "))

    with open("data/menu.json", "r") as file:
        menu = json.load(file)

    for item in menu:

        if item["name"].lower() == food_name.lower():

            price = item["price"]
            total = price * quantity

            order = {
                "id": len(orders) + 1,
                "customer_name": customer_name,
                "food_name": food_name,
                "quantity": quantity,
                "total": total,
                "date": datetime.now().strftime("%d-%m-%Y"),
                "time": datetime.now().strftime("%I:%M:%S %p")
            }

            orders.append(order)

            with open("data/orders.json", "w") as file:
                json.dump(orders, file, indent=4)

            print("\nOrder Details")
            print("Customer Name:", customer_name)
            print("Food Name:", food_name)
            print("Price:", price)
            print("Quantity:", quantity)
            print("Total Amount:", total)
            print("Date:", order["date"])
            print("Time:", order["time"])

            print("\nOrder Placed Successfully!")
            break

    else:
        print("Food Not Found!")


if __name__ == "__main__":
    new_order()
