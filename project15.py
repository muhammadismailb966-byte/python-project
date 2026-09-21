# List of students
students = ["Ali", "Ahmed", "Sara", "Ayesha", "Usman"]

# Dictionary for attendance
attendance = {}


# Record attendance
def record_attendance():
    for student in students:
        status = input(f"Is {student} present? (P/A): ").upper()

        if status == "P":
            attendance[student] = "Present"
        elif status == "A":
            attendance[student] = "Absent"
        else:
            print("Invalid input. Marked as Absent.")
            attendance[student] = "Absent"


# Display attendance
def display_attendance():
    print("\n--- Attendance Record ---")

    for student, status in attendance.items():
        print(student, "-", status)


# Count present and absent students
def count_attendance():
    present = 0
    absent = 0

    for status in attendance.values():
        if status == "Present":
            present += 1
        elif status == "Absent":
            absent += 1

    print("Present Students:", present)
    print("Absent Students:", absent)


# Calculate attendance percentage
def attendance_percentage():
    total_students = len(students)
    present = 0

    for status in attendance.values():
        if status == "Present":
            present += 1

    percentage = (present / total_students) * 100

    print("Attendance Percentage:", percentage, "%")


# Main program
while True:
    print("\n--- Student Attendance System ---")
    print("1. Record Attendance")
    print("2. Display Attendance")
    print("3. Count Present/Absent")
    print("4. Attendance Percentage")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        record_attendance()

    elif choice == "2":
        display_attendance()

    elif choice == "3":
        count_attendance()

    elif choice == "4":
        attendance_percentage()

    elif choice == "5":
        print("Program Ended.")
        break

    else:
        print("Invalid choice.")

# Student Attendance System = List se students + Dictionary se attendance + Loop se checking + Functions se operations + Formula se attendance percentage        