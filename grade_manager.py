FILE_NAME = "students.txt"


def add_student():
    name = input("Enter student name: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{name}\n")

    print("Student added successfully.\n")


def view_students():
    try:
        with open(FILE_NAME, "r") as file:
            print("\nStudents:")
            print("-" * 20)
            for line in file:
                print(line.strip())
            print()
    except FileNotFoundError:
        print("No students found.\n")


def main():
    while True:
        print("Student Grade Manager")
        print("1. Add Student")
        print("2. View Students")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()
