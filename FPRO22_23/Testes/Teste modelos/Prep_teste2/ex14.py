def isomorphic(astring1, astring2):
    if len(astring1) != len(astring2):
        return f"{astring1} and {astring2} are not isomorphic"

    mapping = {}
    mapped_char = set()
    remapped_list = []

    for i, j in zip(astring1, astring2):
        if i not in mapping:
            if j in mapped_char:
                return f"{astring1} and {astring2} are not isomorphic"
            mapping[i] = j
            mapped_char.add(j)
        elif (mapping[i] != j):
            return f"{astring1} and {astring2} are not isomorphic"
        
        remapped_list.append((i, mapping[i]))
    
    return f"{astring1} and {astring2} are isomorphic because we can map:{remapped_list}"


print(isomorphic('ab', 'aa'))
print(isomorphic('paper', 'title'))
print(isomorphic('foo', 'bar'))
print(isomorphic('turtle', 'tletur'))
