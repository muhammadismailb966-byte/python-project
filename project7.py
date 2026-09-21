students = []


def add_student():
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    course = input("Enter student course: ")

    student = {
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)
    print("Student record added successfully!")


def view_students():
    if len(students) == 0:
        print("No student records available.")
    else:
        print("\nAll Students:")

        for i, student in enumerate(students, 1):
            print(i, student["name"], "-", student["age"], "-", student["course"])


def search_student():
    name = input("Enter student name to search: ")

    for student in students:
        if student["name"].lower() == name.lower():
            print("Student Found!")
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Course:", student["course"])
            return

    print("Student not found.")


def update_student():
    name = input("Enter student name to update: ")

    for student in students:
        if student["name"].lower() == name.lower():
            student["age"] = input("Enter new age: ")
            student["course"] = input("Enter new course: ")

            print("Student record updated successfully!")
            return

    print("Student not found.")


def delete_student():
    name = input("Enter student name to delete: ")

    for student in students:
        if student["name"].lower() == name.lower():
            students.remove(student)
            print("Student record deleted successfully!")
            return

    print("Student not found.")


while True:
    print("\n--- Student Record Manager ---")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Program closed!")
        break

    else:
        print("Invalid choice! Try again.")
# concept: List multiple students store karti hai → Dictionary har student ki information rakhti hai → Functions Add, View, Search, Update, Delete perform karte hain → while loop menu ko continuously run karta hai.        