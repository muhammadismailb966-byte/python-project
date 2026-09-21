class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def display(self):
        if self.available:
            status = "Available"
        else:
            status = "Borrowed"

        print(self.title, "-", self.author, "-", status)

    def borrow(self):
        if self.available:
            self.available = False
            print("Book borrowed successfully!")
        else:
            print("Book is already borrowed.")

    def return_book(self):
        if not self.available:
            self.available = True
            print("Book returned successfully!")
        else:
            print("Book is already available.")


books = []


def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")

    book = Book(title, author)
    books.append(book)

    print("Book added successfully!")


def display_books():
    if len(books) == 0:
        print("No books available.")
    else:
        print("\nLibrary Books:")

        for book in books:
            book.display()


def search_book():
    title = input("Enter book title to search: ")

    for book in books:
        if book.title.lower() == title.lower():
            print("Book found!")
            book.display()
            return

    print("Book not found.")


def borrow_book():
    title = input("Enter book title to borrow: ")

    for book in books:
        if book.title.lower() == title.lower():
            book.borrow()
            return

    print("Book not found.")


def return_book():
    title = input("Enter book title to return: ")

    for book in books:
        if book.title.lower() == title.lower():
            book.return_book()
            return

    print("Book not found.")


while True:
    print("\n--- Library Management System ---")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        display_books()

    elif choice == "3":
        search_book()

    elif choice == "4":
        borrow_book()

    elif choice == "5":
        return_book()

    elif choice == "6":
        print("Library program closed!")
        break

    else:
        print("Invalid choice! Try again.")
# concept: Class → Book ka blueprint, Object → actual book, Constructor → book ki information set karta hai, Methods → display/borrow/return ka kaam karte hain, aur List → multiple books store karti hai        