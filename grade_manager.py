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


def add_grades():
    name = input("Enter student name: ")
    subjects = {}

    while True:
        subject = input("Enter subject name (press Enter to finish): ")
        if subject == "":
            break

        try:
            marks = float(input(f"Enter marks for {subject}: "))
        except ValueError:
            print("Invalid marks. Try again.")
            continue

        subjects[subject] = marks

    if not subjects:
        print("No grades added.\n")
        return

    try:
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("No students found.\n")
        return

    with open(FILE_NAME, "w") as file:
        found = False
        for line in lines:
            if line.strip() == name:
                grades = ",".join([f"{s}:{m}" for s, m in subjects.items()])
                file.write(f"{name},{grades}\n")
                found = True
            else:
                file.write(line)

    if found:
        print("Grades added successfully.\n")
    else:
        print("Student not found.\n")


def view_average():
    name = input("Enter student name: ")

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if parts[0] == name and len(parts) > 1:
                    marks = []
                    for item in parts[1:]:
                        _, score = item.split(":")
                        marks.append(float(score))

                    average = sum(marks) / len(marks)
                    print(f"Average marks for {name}: {average}\n")
                    return

            print("Student or grades not found.\n")
    except FileNotFoundError:
        print("No students found.\n")


def main():
    while True:
        print("Student Grade Manager")
        print("1. Add Student")
        print("2. Add Grades")
        print("3. View Students")
        print("4. View Average Grade")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            add_grades()
        elif choice == "3":
            view_students()
        elif choice == "4":
            view_average()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()
