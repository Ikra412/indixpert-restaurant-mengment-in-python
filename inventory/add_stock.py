
import json

def add_stock():

    with open("data/inventory.json", "r") as file:
        stock = json.load(file)

    print("\n----- ADD STOCK -----")

    item_name = input("Enter Item Name: ")
    quantity = int(input("Enter Quantity: "))
    price = float(input("Enter Price: "))

    item = {
        "id": len(stock) + 1,
        "item_name": item_name,
        "quantity": quantity,
        "price": price
    }

    stock.append(item)

    with open("data/inventory.json", "w") as file:
        json.dump(stock, file, indent=4)

    print("\nStock Added Successfully!")


if __name__ == "__main__":
    add_stock()
