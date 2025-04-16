# Get password input from the user
password = input("Enter your password: ")

# Check conditions
has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_digit = any(char.isdigit() for char in password)
is_long_enough = len(password) >= 8

# Final validation
if has_upper and has_lower and has_digit and is_long_enough:
    print("Password is valid.")
else:
    print("Password is invalid.")
    print("Make sure it has at least 1 uppercase letter, 1 lowercase letter, 1 digit, and is at least 8 characters long.")
