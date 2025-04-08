def ticket_price(age):
    if age < 5:
        return "Free"
    elif 5 <= age <= 18:
        return "₹100"
    elif 19 <= age <= 60:
        return "₹200"
    elif age > 60:
        return "₹150"

age = int(input("Enter your age: "))
price = ticket_price(age)


print(f"Ticket price: {price}")
