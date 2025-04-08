
marks = int(input("Enter the marks: "))

if marks >= 290:
    grade = 'A'
elif marks >= 280:
    grade = 'B'
elif marks >= 270:
    grade = 'C'
elif marks >= 260:
    grade = 'D'
else:
    grade = 'F'


print(f"The grade is: {grade}")
