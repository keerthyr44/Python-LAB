# Sample dictionary
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

try:
    key = input("Enter a key (name, age, city): ")
    print("Value:", my_dict[key])
except KeyError:
    print("Error: That key does not exist in the dictionary.")
