even_squares = [x**2 for x in range(1, 21) if x % 2 == 0]


sum_of_squares = sum(even_squares)

print("List of squares of even numbers:", even_squares)
print("Sum:",sum_of_squares)
