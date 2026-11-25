
import json

def view_stock():

    with open("data/inventory.json", "r") as file:
        stock = json.load(file)

    print("\n")
    print("=" * 60)
    print("                  INVENTORY STOCK")
    print("=" * 60)

    print(f"{'ID':<10}{'ITEM NAME':<20}{'QUANTITY':<15}{'PRICE':<10}")
    print("-" * 60)

    if len(stock) == 0:
        print("Stock is Empty!")

    else:
        for item in stock:

            print(f"{item['id']:<10}{item['item_name']:<20}{item['quantity']:<15}{item['price']:<10}")

    print("=" * 60)

    input("\nPress Enter to go back...")


if __name__ == "__main__":
    view_stock()
