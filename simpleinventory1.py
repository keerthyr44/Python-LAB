inventory = {
    'rose': 10,
    'sunflower': 8,
    'lilly': 15
}

while True:
    print("\nCurrent Inventory:")
    for item, qty in inventory.items():
        print(f"{item.title()}: {qty}")

    # Get user input
    item_name = input("\nEnter the item name to sell (or 'exit' to quit): ").lower()
    if item_name == 'exit':
        print("Exiting the inventory system.")
        break

    if item_name not in inventory:
        print("Item not found in inventory.")
        continue

    try:
        quantity_to_sell = int(input(f"Enter quantity to sell for '{item_name}': "))
        if quantity_to_sell <= 0:
            print("Please enter a positive quantity.")
            continue
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

   
    if inventory[item_name] >= quantity_to_sell:
        inventory[item_name] -= quantity_to_sell
        print(f"Sold {quantity_to_sell} {item_name}(s). Remaining: {inventory[item_name]}")
    else:
        print(f"Not enough {item_name}s in stock. Only {inventory[item_name]} left.")
