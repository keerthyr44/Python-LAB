# Student data structure: (Name, Roll Number, (Marks in 3 Subjects), Grade)

# Sample student list
students = [
    ("Deepthi", 101, (85, 90, 78), "A"),
    ("Bindu", 102, (70, 75, 80), "B"),
    ("Keerthy", 103, (60, 65, 58), "C")
]

def display_all_students(student_list):
    print("\nAll Students:")
    for student in student_list:
        print(student)

def add_student(student_list, name, roll_number, marks, grade):
    student_list.append((name, roll_number, marks, grade))
    print(f"Student {name} added.")

def search_student(student_list, roll_number):
    for student in student_list:
        if student[1] == roll_number:
            print(f"Student Found: {student}")
            return student
    print("Student not found.")
    return None

def calculate_total_marks(student_list):
    print("\nTotal Marks for Each Student:")
    for student in student_list:
        total = sum(student[2])
        print(f"{student[0]} (Roll: {student[1]}): Total Marks = {total}")

def update_grade(student_list, roll_number, new_grade):
    for i in range(len(student_list)):
        if student_list[i][1] == roll_number:
            student = student_list[i]
            updated_student = (student[0], student[1], student[2], new_grade)
            student_list[i] = updated_student
            print(f"Grade updated for Roll Number {roll_number}.")
            return
    print("Student not found.")

def remove_student(student_list, roll_number):
    for i in range(len(student_list)):
        if student_list[i][1] == roll_number:
            removed = student_list.pop(i)
            print(f"Removed student: {removed}")
            return
    print("Student not found.")


display_all_students(students)
add_student(students, "Divya", 104, (88, 77, 66), "B")
search_student(students, 102)
calculate_total_marks(students)
update_grade(students, 103, "B+")
remove_student(students, 101)
display_all_students(students)
