numbers=[23,45,76,90]
largest=numbers[0]
smallest=numbers[0]

for num in numbers:
    if num>largest:
        largest=num
    elif num<smallest:
        smallest=num
print("List:",numbers)
print("Largest number:",largest)
print("Smallest number:",smallest)
