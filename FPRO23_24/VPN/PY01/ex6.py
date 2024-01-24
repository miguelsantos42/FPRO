import math
air = -10
velocity = 18

angle = int(input())

converted_angle = math.radians(angle)

horizontal_distance = (math.pow(velocity,2) * math.sin(2*converted_angle))/(-air)

print(round(horizontal_distance))