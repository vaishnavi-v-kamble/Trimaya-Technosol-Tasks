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
