class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        avg = self.average_grade()
        grade_list = ", ".join(map(str, self.grades))
        return f"Student: {self.name}\nGrades: {grade_list}\nAverage: {avg:.2f}\n"


class GradingSystem:
    def __init__(self):
        self.students = []

    def add_student(self, name):
        student = Student(name)
        self.students.append(student)
        print(f"Student '{name}' added successfully!")

    def add_grade_to_student(self, name, grade):
        for student in self.students:
            if student.name == name:
                student.add_grade(grade)
                print(f"Grade {grade} added to {name}.")
                return
        print(f"Student '{name}' not found.")

    def show_all_results(self):
        if not self.students:
            print("No students found.")
        else:
            print("\n--- Student Grades ---")
            for student in self.students:
                print(student)


def main():
    system = GradingSystem()

    while True:
        print("\n==== Student Grading System ====")
        print("1. Add Student")
        print("2. Add Grade to Student")
        print("3. Show All Results")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            name = input("Enter student name: ")
            system.add_student(name)

        elif choice == "2":
            name = input("Enter student name: ")
            try:
                grade = float(input("Enter grade: "))
                system.add_grade_to_student(name, grade)
            except ValueError:
                print("Invalid grade. Please enter a number.")

        elif choice == "3":
            system.show_all_results()

        elif choice == "4":
            print("Exiting system")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
