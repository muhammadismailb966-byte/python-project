balance = 5000


def check_balance():
    print("Your balance is:", balance)


def deposit():
    global balance

    try:
        amount = float(input("Enter deposit amount: "))

        if amount > 0:
            balance += amount
            print("Money deposited successfully!")
            print("New balance:", balance)
        else:
            print("Amount must be greater than 0.")

    except ValueError:
        print("Invalid input! Please enter a number.")


def withdraw():
    global balance

    try:
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Amount must be greater than 0.")

        elif amount > balance:
            print("Insufficient balance!")

        else:
            balance -= amount
            print("Money withdrawn successfully!")
            print("Remaining balance:", balance)

    except ValueError:
        print("Invalid input! Please enter a number.")


while True:
    print("\n--- ATM Menu ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        check_balance()

    elif choice == "2":
        deposit()

    elif choice == "3":
        withdraw()

    elif choice == "4":
        print("Thank you for using ATM!")
        break

    else:
        print("Invalid choice! Please try again.")
# concept: balance money store karta hai → Functions ATM operations perform karte hain → if/elif menu aur conditions handle karta hai → try/except invalid input handle karta hai → withdrawal balance se zyada ho to Insufficient balance → while loop ATM ko continuously running rakhta hai        
