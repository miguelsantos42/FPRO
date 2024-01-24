from math import sqrt

a = float(input())
b = float(input())
c = float(input())

x1 = ((-b + sqrt(b**2 - 4 * a * c))/(2*a))
x2 = ((-b - sqrt(b**2 - 4 * a * c))/(2*a))

print(f"The solutions are {round(x1,2)} and {round(x2,2)}")

