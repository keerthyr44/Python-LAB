def calculate_square_and_cube(number):
    square=number**2
    cube=number**3
    return square,cube

number=float(input("Enter a number:"))
square,cube=calculate_square_and_cube(number)

print(f"The Square of {number}is:{square}")
print(f"The Cube of {number}is:{cube}")

