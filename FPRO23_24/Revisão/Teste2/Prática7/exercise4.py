def isomorphic(astring1, astring2):
    dici1 = {}

    for i in range(len(astring1)):
        if astring1[i] not in dici1.keys() and astring2[i] not in dici1.values():
            dici1[astring1[i]] = astring2[i]
        elif astring1[i] in dici1.keys():
            if dici1[astring1[i]] != astring2[i]:
                return (f"'{astring1}' and '{astring2}' are not isomorphic")
        elif astring1[i] not in dici1.keys():
            if astring2[i] in dici1.values():
                return (f"'{astring1}' and '{astring2}' are not isomorphic")

    # dici1 = {}

    # for i in range(len(astring2)):
    #     if astring2[i] not in dici1.keys() and astring1[i] not in dici1.values():
    #         dici1[astring2[i]] = astring1[i]
    #     elif astring2[i] in dici1.keys():
    #         if dici1[astring2[i]] != astring1[i]:
    #             return (f"{astring1} and {astring2} are not isomorphic")
    
    return (f"'{astring1}' and '{astring2}' are isomorphic")


print(isomorphic('ab', 'aa'))
print(isomorphic('paper', 'title'))
print(isomorphic('foo', 'bar'))
print(isomorphic('turtle', 'tletur'))
