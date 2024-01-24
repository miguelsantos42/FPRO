def adigits(a, b, c):
    final_num = 0
    if(a <= b and b <= c):
        final_num = final_num + a*100 + b*10 + c
    elif(a <= c and c <= b):
        final_num = final_num + a*100 + c*10 + b
    elif(b <= a and a <= c):
        final_num = final_num + b*100 + a*10 + c
    elif(b <= c and c <= a):
        final_num = final_num + b*100 + c*10 + a
    elif(c <= a and a <= b):
        final_num = final_num + c*100 + a*10 + b
    else:
        final_num = final_num + c*100 + b*10 + a
    return final_num

print(adigits(1, 2, 3))
print(adigits(9, 1, 9))
print(adigits(9, 1, 8))
print(adigits(0, 1, 0))
