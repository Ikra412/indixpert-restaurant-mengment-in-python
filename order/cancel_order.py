
import json

def cancel_order():

    with open("data/orders.json", "r") as file:
        orders = json.load(file)

    print("\n----- CANCEL ORDER -----")

    order_id = int(input("Enter Order ID: "))

    for order in orders:

        if order["id"] == order_id:

            print("\nCustomer Name:", order["customer_name"])
            print("Food Name:", order["food_name"])
            print("Quantity:", order["quantity"])
            print("Total Amount:", order["total"])

            choice = input("\nDo you want to cancel this order? (yes/no): ")

            if choice.lower() == "yes":

                orders.remove(order)

                with open("data/orders.json", "w") as file:
                    json.dump(orders, file, indent=4)

                print("\nOrder Cancelled Successfully!")

            else:
                print("\nOrder Not Cancelled!")

            break

    else:
        print("\nOrder Not Found!")


if __name__ == "__main__":
    cancel_order()
