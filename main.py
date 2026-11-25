
from authentication.admin_login import admin_login
from authentication.staff_login import staff_login
from authentication.logout import logout

from menu.add_menu import add_menu
from menu.update_menu import update_menu
from menu.delete_menu import delete_menu
from menu.view_menu import view_menu

from order.new_order import new_order
from order.update_order import update_order
from order.cancel_order import cancel_order
from order.view_order import view_order

from billing.generate_bill import generate_bill

from table_booking.book_table import book_table
from table_booking.available_tables import available_tables
from table_booking.booking_status import booking_status

from inventory.add_stock import add_stock
from inventory.update_stock import update_stock
from inventory.view_stock import view_stock


while True:

    print("\n")
    print("=" * 45)
    print("       RESTAURANT MANAGEMENT SYSTEM")
    print("=" * 45)

    print("1. Admin Login")
    print("2. Staff Login")
    print("3. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        if admin_login():

            while True:

                print("\n----- ADMIN DASHBOARD -----")

                print("1. Add Menu")
                print("2. Update Menu")
                print("3. Delete Menu")
                print("4. View Menu")

                print("5. New Order")
                print("6. Update Order")
                print("7. Cancel Order")
                print("8. View Orders")

                print("9. Generate Bill")

                print("10. Book Table")
                print("11. Available Tables")
                print("12. Booking Status")

                print("13. Add Stock")
                print("14. Update Stock")
                print("15. View Stock")

                print("16. Logout")

                choice = input("\nEnter your choice: ")

                if choice == "1":
                    add_menu()

                elif choice == "2":
                    update_menu()

                elif choice == "3":
                    delete_menu()

                elif choice == "4":
                    view_menu()

                elif choice == "5":
                    new_order()

                elif choice == "6":
                    update_order()

                elif choice == "7":
                    cancel_order()

                elif choice == "8":
                    view_order()

                elif choice == "9":
                    generate_bill()

                elif choice == "10":
                    book_table()

                elif choice == "11":
                    available_tables()

                elif choice == "12":
                    booking_status()

                elif choice == "13":
                    add_stock()

                elif choice == "14":
                    update_stock()

                elif choice == "15":
                    view_stock()

                elif choice == "16":
                    logout()
                    break

                else:
                    print("\nInvalid Choice!")


    elif choice == "2":

        if staff_login():

            while True:

                print("\n----- STAFF DASHBOARD -----")

                print("1. View Menu")
                print("2. New Order")
                print("3. View Orders")
                print("4. Book Table")
                print("5. Booking Status")
                print("6. View Stock")
                print("7. Logout")

                choice = input("\nEnter your choice: ")

                if choice == "1":
                    view_menu()

                elif choice == "2":
                    new_order()

                elif choice == "3":
                    view_order()

                elif choice == "4":
                    book_table()

                elif choice == "5":
                    booking_status()

                elif choice == "6":
                    view_stock()

                elif choice == "7":
                    logout()
                    break

                else:
                    print("\nInvalid Choice!")


    elif choice == "3":

        print("\nThank You!")
        break

    else:
        print("\nInvalid Choice! Please Try Again.")
