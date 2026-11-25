
import json

def generate_bill():

    with open("data/orders.json", "r") as file:
        orders = json.load(file)

    with open("data/bills.json", "r") as file:
        bills = json.load(file)

    print("\n----- GENERATE BILL -----")

    order_id = int(input("Enter Order ID: "))

    for order in orders:

        if order["id"] == order_id:

            bill = {
                "bill_id": len(bills) + 1,
                "order_id": order["id"],
                "customer_name": order["customer_name"],
                "food_name": order["food_name"],
                "quantity": order["quantity"],
                "total": order["total"]
            }

            bills.append(bill)

            with open("data/bills.json", "w") as file:
                json.dump(bills, file, indent=4)

            print("\n----- BILL DETAILS -----")
            print("Bill ID:", bill["bill_id"])
            print("Customer Name:", bill["customer_name"])
            print("Food Name:", bill["food_name"])
            print("Quantity:", bill["quantity"])
            print("Total Amount:", bill["total"])
            print("------------------------")
            print("Bill Generated Successfully!")

            break

    else:
        print("Order Not Found!")


if __name__ == "__main__":
    generate_bill()
