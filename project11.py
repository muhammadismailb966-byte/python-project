rooms = {
    101: None,
    102: None,
    103: None,
    104: None,
    105: None
}


def display_rooms():
    print("\n--- Room Status ---")

    for room, customer in rooms.items():
        if customer is None:
            print(room, "- Available")
        else:
            print(room, "- Booked by", customer)


def book_room():
    room = int(input("Enter room number: "))

    if room not in rooms:
        print("Room does not exist.")

    elif rooms[room] is not None:
        print("Room is already booked!")

    else:
        name = input("Enter customer name: ")
        rooms[room] = name
        print("Room booked successfully!")


def cancel_booking():
    room = int(input("Enter room number to cancel: "))

    if room not in rooms:
        print("Room does not exist.")

    elif rooms[room] is None:
        print("Room is not booked.")

    else:
        rooms[room] = None
        print("Booking cancelled successfully!")


def search_booking():
    name = input("Enter customer name to search: ")

    found = False

    for room, customer in rooms.items():
        if customer is not None and customer.lower() == name.lower():
            print("Booking found!")
            print("Customer:", customer)
            print("Room:", room)
            found = True

    if not found:
        print("Booking not found.")


while True:
    print("\n--- Hotel Room Booking System ---")
    print("1. Display Rooms")
    print("2. Book Room")
    print("3. Cancel Booking")
    print("4. Search Booking")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_rooms()

    elif choice == "2":
        try:
            book_room()
        except ValueError:
            print("Invalid room number!")

    elif choice == "3":
        try:
            cancel_booking()
        except ValueError:
            print("Invalid room number!")

    elif choice == "4":
        search_booking()

    elif choice == "5":
        print("Hotel Booking System closed!")
        break

    else:
        print("Invalid choice! Try again.")
# concept: Dictionary rooms store karti hai → Functions booking operations perform karte hain → Conditions availability check karti hain → double booking prevent hoti hai → booking cancel ho sakti hai → customer name se booking search ho sakti hai        