
import json

def view_order():

    with open("data/orders.json", "r") as file:
        orders = json.load(file)

    print("\n----- ALL ORDERS -----")

    if len(orders) == 0:
        print("No Orders Found!")

    else:
        for order in orders:

            print("\nOrder ID:", order["id"])
            print("Customer Name:", order["customer_name"])
            print("Food Name:", order["food_name"])
            print("Quantity:", order["quantity"])
            print("Total Amount:", order["total"])
            print("Date:", order.get("date", "Not Available"))
            print("Time:", order.get("time", "Not Available"))
            print("----------------------------")

    input("\nPress Enter to go back...")


if __name__ == "__main__":
    view_order()
