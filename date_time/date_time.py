
from datetime import datetime

def show_date_time():

    now = datetime.now()

    date = now.strftime("%d-%m-%Y")
    time = now.strftime("%I:%M:%S %p")

    print("\n----- DATE AND TIME -----")
    print("Date:", date)
    print("Time:", time)


if __name__ == "__main__":
    show_date_time()
