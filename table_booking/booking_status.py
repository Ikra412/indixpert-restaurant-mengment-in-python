
import json

def booking_status():

    with open("data/bookings.json", "r") as file:
        bookings = json.load(file)

    print("\n----- BOOKING STATUS -----")

    booking_id = int(input("Enter Booking ID: "))

    for booking in bookings:

        if booking["id"] == booking_id:

            print("\nBooking Details")
            print("Customer Name:", booking["customer_name"])
            print("Table Number:", booking["table_number"])
            print("Booking Date:", booking["date"])
            print("Booking Time:", booking["time"])
            print("Status:", booking["status"])
            print("Created Date:", booking.get("created_date", "Not Available"))
            print("Created Time:", booking.get("created_time", "Not Available"))

            break

    else:
        print("\nBooking Not Found!")

    input("\nPress Enter to go back...")


if __name__ == "__main__":
    booking_status()
