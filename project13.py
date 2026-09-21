def km_to_miles():
    km = float(input("Enter kilometers: "))
    miles = km * 0.621371
    print("Miles:", miles)


def miles_to_km():
    miles = float(input("Enter miles: "))
    km = miles * 1.60934
    print("Kilometers:", km)


def kg_to_pounds():
    kg = float(input("Enter kilograms: "))
    pounds = kg * 2.20462
    print("Pounds:", pounds)


def pounds_to_kg():
    pounds = float(input("Enter pounds: "))
    kg = pounds * 0.453592
    print("Kilograms:", kg)


def celsius_to_fahrenheit():
    celsius = float(input("Enter Celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32
    print("Fahrenheit:", fahrenheit)


def fahrenheit_to_celsius():
    fahrenheit = float(input("Enter Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9
    print("Celsius:", celsius)


while True:
    print("\n--- Unit Conversion System ---")
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    print("3. Kilograms to Pounds")
    print("4. Pounds to Kilograms")
    print("5. Celsius to Fahrenheit")
    print("6. Fahrenheit to Celsius")
    print("7. Exit")

    choice = input("Enter your choice: ")

    try:
        if choice == "1":
            km_to_miles()

        elif choice == "2":
            miles_to_km()

        elif choice == "3":
            kg_to_pounds()

        elif choice == "4":
            pounds_to_kg()

        elif choice == "5":
            celsius_to_fahrenheit()

        elif choice == "6":
            fahrenheit_to_celsius()

        elif choice == "7":
            print("Program closed!")
            break

        else:
            print("Invalid choice! Please select 1-7.")

    except ValueError:
        print("Invalid input! Please enter a number.")
# concept: Menu se conversion select hoti hai → user value enter karta hai → separate function conversion perform karta hai → result display hota hai → try/except invalid input handle karta hai        