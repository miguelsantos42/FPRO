def add(num1, num2):
    num1 = num1.split('.')
    num2 = num2.split('.')

    #decimal
    num3 = ""

    if len(num1[1]) > len(num2[1]):
        for i in range(len(num2[1]), len(num1[1])):
            num2[1] += '0'
    else:
        for j in range(len(num1[1]), len(num2[1])):
            num1[1] += '0'
    
    carry = 0
    for i in range(len(num1[1])-1,-1,-1):
        num3 = str((int(num1[1][i]) + int(num2[1][i]) + carry)%10) + num3
        carry = (int(num1[1][i]) + int(num2[1][i]) + carry)//10
    num3 = "." + num3
    num3 = num3.rstrip('0')

    if len(num3) == 1:
        num3 += '0'

    #inteira
    if len(num1[0]) > len(num2[0]):
        for i in range(len(num2[0]), len(num1[0])):
            num2[0] = '0' + num2[0]
    else:
        for j in range(len(num1[0]), len(num2[0])):
            num1[0] = '0' + num1[0]
    
    
    for i in range(len(num1[0])-1,-1,-1):
        num3 = str((int(num1[0][i]) + int(num2[0][i]) + carry)%10) + num3
        carry = (int(num1[0][i]) + int(num2[0][i]) + carry)//10
    if carry > 0:
        num3 = str(carry) + num3

    num3 = num3.lstrip('0')

    return num3

# print(add('123.456', '0.124'))
# print(add('0123.40', '0.567'))
# print(add('123.45', '1000.55'))
# print(add('123456789.0', '0.00000000000001'))

    
    
    