def roman_to_integer(astring):
    total = 0

    romans = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
    
    for i in range(0, len(astring)-1):
        if romans.get(astring[i]) < romans.get(astring[i+1]):
            total -= romans.get(astring[i])
        else:
            total += romans.get(astring[i])

    return total + romans.get(astring[-1])

print(roman_to_integer('XV'))
print(roman_to_integer('LXXXIV'))
print(roman_to_integer('XLIII'))
print(roman_to_integer('MMMCMXCIX'))
