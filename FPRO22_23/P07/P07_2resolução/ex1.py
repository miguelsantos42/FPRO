def switch_dict(adict):
    dici = {}
    for k, v in adict.items():
        if v not in dici:
            dici[v] = [k]
        else:
            dici[v].append(k)
    return dici

print(switch_dict({"jan": "winter", "feb": "winter", "may": "spring", "july": "summer", "august": "summer"}))
print(switch_dict({1: 2, 2: 1, 3: 1, 4: 2}))
