import random

def get_numbers_ticket(min, max, quantity):
    has_error = False

    if min < 1:
        print("Minimum must be ≥ 1!")
        has_error = True
    
    if max > 1000:
        print("Maximum must be ≤ 1000!")
        has_error = True
    
    if min > max:
        print("Minimum must not exceed maximum!")
        has_error = True
    
    if quantity < 1 or quantity > (max - min + 1):
        print("Quantity must be within the valid range!")
        has_error = True

    if has_error:
        print()
        return []

    return sorted(random.sample(range(min, max + 1), quantity))

while True:
    try:
        min_number = int(input("Enter the minimum number (at least 1): "))
        max_number = int(input("Enter the maximum number (no more than 1000): "))
        quantity_number = int(input(f"Enter the quantity of numbers to pick (between {min_number} and {max_number}): "))
       

        lottery_numbers = get_numbers_ticket(min_number, max_number, quantity_number)
        if lottery_numbers:
            print(f"\nYour lottery numbers: {lottery_numbers}")
            break
        else:
            print("Please try again!")
    except ValueError:
        print("Error! Please enter a number!\n")