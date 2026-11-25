
import json
from datetime import datetime

def book_table():

    with open("data/bookings.json", "r") as file:
        bookings = json.load(file)

    print("\n----- BOOK TABLE -----")

    customer_name = input("Enter Customer Name: ")
    table_number = int(input("Enter Table Number: "))
    date = input("Enter Booking Date: ")
    time = input("Enter Booking Time: ")

    booking = {
        "id": len(bookings) + 1,
        "customer_name": customer_name,
        "table_number": table_number,
        "date": date,
        "time": time,
        "status": "Booked",
        "created_date": datetime.now().strftime("%d-%m-%Y"),
        "created_time": datetime.now().strftime("%I:%M:%S %p")
    }

    bookings.append(booking)

    with open("data/bookings.json", "w") as file:
        json.dump(bookings, file, indent=4)

    print("\nTable Booked Successfully!")
    print("Booking Date:", date)
    print("Booking Time:", time)
    print("Created Date:", booking["created_date"])
    print("Created Time:", booking["created_time"])


if __name__ == "__main__":
    book_table()
