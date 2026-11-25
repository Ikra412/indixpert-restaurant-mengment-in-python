
import json

def update_stock():

    with open("data/inventory.json", "r") as file:
        stock = json.load(file)

    print("\n----- UPDATE STOCK -----")

    item_id = int(input("Enter Item ID: "))

    for item in stock:

        if item["id"] == item_id:

            print("\nItem Name:", item["item_name"])
            print("Current Quantity:", item["quantity"])
            print("Current Price:", item["price"])

            new_quantity = int(input("Enter New Quantity: "))
            new_price = float(input("Enter New Price: "))

            item["quantity"] = new_quantity
            item["price"] = new_price

            with open("data/inventory.json", "w") as file:
                json.dump(stock, file, indent=4)

            print("\nStock Updated Successfully!")
            break

    else:
        print("\nItem Not Found!")


if __name__ == "__main__":
    update_stock()
