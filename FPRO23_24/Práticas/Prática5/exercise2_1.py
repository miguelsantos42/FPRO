def camel_case(phrase):
    flag = False
    new_str = ""
    for c in phrase:
        if c.isalpha():
            if flag:
                new_str += c.upper()
                flag=False
            else:
                new_str += c.lower()
        else:
            flag = True
