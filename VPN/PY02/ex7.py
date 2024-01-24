dist = float(input())
liters = float(input())
price_per_liter = float(input())

waste_fuel = (dist * liters)/100

print(round(waste_fuel * price_per_liter,2))


