def isomorphic(astring1, astring2):
    dici = {}

    for i in range(len(astring1)):
        if(astring1[i] not in dici.keys() and astring2 not in dici.values()):
            dici[astring1[i]] = astring2[i]
        elif(astring1 in dici.keys()):
            if(astring2 not in dici.values()):
                return(f"'{astring1}' and '{astring2}' are not isomorphic")
        elif(astring1 not in dici.keys()):
            if(astring2 in dici.values()):
                return(f"'{astring1}' and '{astring2}' are not isomorphic")
    
    return(f"'{astring1}' and '{astring2}' are isomorphic")


print(isomorphic('ab', 'aa'))
print(isomorphic('paper', 'title'))
print(isomorphic('foo', 'bar'))
print(isomorphic('turtle', 'tletur'))


