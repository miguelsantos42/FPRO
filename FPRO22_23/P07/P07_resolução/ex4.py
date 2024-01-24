def isomorphic(astring1,astring2):
    if len(astring1) != len(astring2):
        return(f"{astring1} and {astring2} are not isomorphic")
    
    mapping = {}
    mapped_chars = set()
    remapped_chars = []

    for char1, char2 in zip(astring1, astring2): #zip permite iterar sobre duas tuplas ao mesmo tempo
        if char1 not in mapping:
            if char2 in mapped_chars:
                return(f"{astring1} and {astring2} are not isomorphic")
            mapping[char1] = char2
            mapped_chars.add(char2)
        elif mapping[char1] != char2:
            return(f"{astring1} and {astring2} are not isomorphic")
        
        remapped_chars.append((char1, mapping[char1]))

    return(f"{astring1} and {astring2} are isomorphic because we can map: {remapped_chars}")


print(isomorphic('ab', 'aa'))
print(isomorphic('paper', 'title'))
print(isomorphic('foo', 'bar'))
print(isomorphic('turtle', 'tletur'))
