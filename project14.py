# Product list
products = {
    "apple": 100,
    "milk": 200,
    "bread": 150,
    "eggs": 250
}

cart = []


# Add product
def add_product():
    product = input("Enter product name: ").lower()

    if product in products:
        cart.append(product)
        print(product, "added to cart.")
    else:
        print("Product not available.")


# Remove product
def remove_product():
    product = input("Enter product name to remove: ").lower()

    if product in cart:
        cart.remove(product)
        print(product, "removed from cart.")
    else:
        print("Product is not in cart.")


# Display cart
def display_cart():
    if len(cart) == 0:
        print("Cart is empty.")
    else:
        print("\nYour Cart:")
        for product in cart:
            print(product, "-", products[product])


# Calculate total bill
def calculate_bill():
    total = 0

    for product in cart:
        total = total + products[product]

    print("Total Bill =", total)


# Main menu
while True:
    print("\n--- Shopping Cart ---")
    print("1. Add Product")
    print("2. Remove Product")
    print("3. Display Cart")
    print("4. Calculate Bill")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_product()

    elif choice == "2":
        remove_product()

    elif choice == "3":
        display_cart()

    elif choice == "4":
        calculate_bill()

    elif choice == "5":
        print("Thank you for shopping!")
        break

    else:
        print("Invalid choice.")
# Concept
# Shopping Cart = Dictionary se products/prices + List se cart + Functions se operations + Loops se menu aur bill calculation.        