class Product:

    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def display(self):
        print(self.name, "-", self.price, "-", self.stock)


products = []


def add_product():
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    stock = int(input("Enter stock quantity: "))

    product = Product(name, price, stock)
    products.append(product)

    print("Product added successfully!")


def view_products():
    if len(products) == 0:
        print("No products available.")
    else:
        print("\nProducts:")
        for product in products:
            product.display()


def search_product():
    name = input("Enter product name to search: ")

    for product in products:
        if product.name.lower() == name.lower():
            print("Product found!")
            product.display()
            return

    print("Product not found.")


def update_stock():
    name = input("Enter product name: ")

    for product in products:
        if product.name.lower() == name.lower():
            quantity = int(input("Enter new stock quantity: "))
            product.stock = quantity
            print("Stock updated successfully!")
            return

    print("Product not found.")


def remove_product():
    name = input("Enter product name to remove: ")

    for product in products:
        if product.name.lower() == name.lower():
            products.remove(product)
            print("Product removed successfully!")
            return

    print("Product not found.")


def total_inventory_value():
    total = 0

    for product in products:
        total += product.price * product.stock

    print("Total Inventory Value:", total)


while True:
    print("\n--- Product Inventory System ---")
    print("1. Add Product")
    print("2. View Products")
    print("3. Search Product")
    print("4. Update Stock")
    print("5. Remove Product")
    print("6. Total Inventory Value")
    print("7. Exit")

    choice = input("Enter your choice: ")

    try:
        if choice == "1":
            add_product()

        elif choice == "2":
            view_products()

        elif choice == "3":
            search_product()

        elif choice == "4":
            update_stock()

        elif choice == "5":
            remove_product()

        elif choice == "6":
            total_inventory_value()

        elif choice == "7":
            print("Inventory System closed!")
            break

        else:
            print("Invalid choice!")

    except ValueError:
        print("Invalid input! Please enter correct values.")
# concept: Class → Product ka blueprint, Object → actual product, Properties → name/price/stock, Methods → product operations, List → multiple products store karti hai, aur price × stock se total inventory value calculate hoti hai        