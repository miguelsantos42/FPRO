tS = float(input())
tC = float(input())
tR = float(input())

vS = 1.5/tS
vC = 40/tC
vR = 10/tR

total_time = tS + tC + tR

if total_time > 4:
    print("Time")
elif vR < 8:
    print("Running")
elif vC < 20:
    print("Cycling")
elif vS < 2:
    print("Swimming")
else:
    print(total_time)