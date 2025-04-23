# Predefined list
my_list = [10, 20, 30, 40, 50]

try:
    # Ask the user for an index
    index = int(input("Enter an index to retrieve the value from the list: "))
    
    # Print the value at the given index
    print("Value at index", index, "is", my_list[index])

except IndexError:
    print("Error: The index you entered is out of range.")

except ValueError:
    print("Error: Please enter a valid integer index.")
