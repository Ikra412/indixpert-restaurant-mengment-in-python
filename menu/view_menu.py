
import json
def view_menu():

    with open("data/menu.json", "r") as file:
        menu = json.load(file)

    print("\n")
    print("=" * 65)
    print("                    RESTAURANT MENU")
    print("=" * 65)

    print(f"{'ID':<10}{'FOOD NAME':<20}{'PRICE':<15}{'QUANTITY':<10}")
    print("-" * 65)

    for item in menu:
        print(f"{item['id']:<10}{item['name']:<20}{item['price']:<15}{item.get('quantity', 0):<10}")

    print("=" * 65)
    input("\nPress Enter to go back...")


if __name__ == "__main__":
    view_menu()
