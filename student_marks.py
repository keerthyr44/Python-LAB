student_marks={
    "keerthy":90,
    "Monsiha":78,
    "Bhavya":67,
    "Archana":45,
    }

name=(input("Enter the student name:"))

if name in student_marks:
    print(f"{name}'s marks:{student_marks[name]}")
else:
    print(f"No record found for student:'{name}'")
