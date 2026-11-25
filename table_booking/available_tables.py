
import json

def available_tables():

    with open("data/bookings.json", "r") as file:
        bookings = json.load(file)

    print("\n----- TABLE STATUS -----")

    total_tables = 10

    for table in range(1, total_tables + 1):

        booked = False

        for booking in bookings:

            if booking["table_number"] == table and booking["status"] == "Booked":
                booked = True
                break

        if booked:
            print("Table", table, "- Booked")
        else:
            print("Table", table, "- Available")


if __name__ == "__main__":
    available_tables()
