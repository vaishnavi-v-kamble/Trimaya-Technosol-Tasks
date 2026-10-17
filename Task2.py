'''Task 3: Apply Membership Discount 
Objective: Adjust the base_fee by applying a membership discount if applicable.
Steps: 1. Prompt the user to enter their membership type (Premium, Standard, or None).
        2. Use conditional statements to determine the discount rate: - Premium: 15% discount - Standard: 10% discount - None: No discount 
        3. If the membership type is invalid, display an error and exit. 
        4. Calculate the discount amount and subtract it from the base_fee. 
Expected Output: The adjusted fee after the membership discount. '''

print('''car rents = Economy having $50/day
Standard having $75/day
Luxury having $100/day''')

car_type = input("enter the car type(Economy, Standard, Luxury)").lower()
rent_days = int(input("rent days:"))

if car_type=='economy':
    car_rent = rent_days * 50
    print('car rent for',rent_days,'is',car_rent)

elif car_type=='standard':
    car_rent = rent_days * 75
    print('car rent for',rent_days,'is',car_rent)

elif car_type=='luxury':
    car_rent = rent_days * 100
    print('car rent for',rent_days,'is',car_rent)
    
else:
    print("invalid car type choice !!")
    raise SystemExit(1)

base_fee = car_rent
membership_type = input("Enter membership type (Premium, Standard, or None): ").strip().lower()

if membership_type == 'premium':
    discount_rate = 0.15
elif membership_type == 'standard':
    discount_rate = 0.10
elif membership_type == 'none':
    discount_rate = 0
else:
    print("Invalid membership type choice !!")
    raise SystemExit(1)

discount_amount = base_fee * discount_rate
adjusted_fee = base_fee - discount_amount
print("Adjusted fee after membership discount:", adjusted_fee)
