# module.py
def get_student_data():
    """Returns a dictionary containing sample student data."""
    students = {
        'Muhammad Bilal': {'age': 23, 'grades': [90, 85, 95]},
        'Aliza': {'age': 22, 'grades': [88, 92, 89]},
        'Saba': {'age': 20, 'grades': [75, 80, 79]},
        'Shazil': {'age': 24, 'grades': [82, 77, 90]}
    }
    return students

def filter_students(students, grade_threshold):
    """Returns a list of students whose average grade is above the grade_threshold."""
    filtered_students = []
    for name, data in students.items():
        avg_grade = sum(data['grades']) / len(data['grades'])
        if avg_grade > grade_threshold:
            filtered_students.append((name, data['age'], data['grades']))
    return filtered_students

def calculate_average_grade(students):
    """Calculates the average grade for all students."""
    total_grades = 0
    total_subjects = 0
    for data in students.values():
        total_grades += sum(data['grades'])
        total_subjects += len(data['grades'])
    return total_grades / total_subjects if total_subjects > 0 else 0

def sort_students(students):
    """Sorts students by their age and returns a sorted list of (name, age, grades)."""
    sorted_students = sorted(students.items(), key=lambda x: x[1]['age'])
    return [(name, data['age'], data['grades']) for name, data in sorted_students]

# explorer.py
from module import get_student_data, filter_students, calculate_average_grade, sort_students

def explorer():
    """Main function for student data exploration."""
    students = get_student_data()

    while True:
        print("\nStudent Explorer\n----------------")
        print("1. View all students")
        print("2. Filter students by grade")
        print("3. Calculate average grade")
        print("4. Exit")

        choice = input("Choose an option: ")
        
        if choice == '1':
            print("\nName        | Age | Grades")
            print("----------- | --- | --------")
            for name, data in students.items():
                print(f"{name:<11} | {data['age']}  | {data['grades']}")
        
        elif choice == '2':
            try:
                grade_threshold = float(input("\nGrade Threshold: "))
                filtered = filter_students(students, grade_threshold)
                if filtered:
                    print("\nFiltered Students:\n------------------")
                    print("Name        | Age | Grades")
                    print("----------- | --- | --------")
                    for name, age, grades in filtered:
                        print(f"{name:<11} | {age}  | {grades}")
                else:
                    print("\nNo students found above the threshold.")
            except ValueError:
                print("\nPlease enter a valid number for the grade threshold.")
        
        elif choice == '3':
            avg_grade = calculate_average_grade(students)
            print(f"\nThe average grade for all students is: {avg_grade:.2f}")
        
        elif choice == '4':
            print("\nHave a good experience with explorer.")
            break
        
        else:
            print("\n Your input is not match with any of the above choices plz try with valid number.")

if _name_ == "_main_":
    explorer()