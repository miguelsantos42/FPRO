def check_results(bet, results):
    total = 0
    for i in range(0,len(bet)):
        if bet[i] == 'X' and (results[i][2] == results[i][3]):
            total = total + 1
        elif bet[i] == '1' and (results[i][2] > results[i][3]):
            total = total + 1
        elif bet[i] == '2' and (results[i][2] < results[i][3]):
            total = total + 1
        else:
            continue
    return total



print(check_results("XX121X221X122", [("Team A","Team B",0,0),
    ("Team C","Team D",2,1), ("Team E","Team F",0,4), 
    ("Team G","Team H",1,1), ("Team I","Team J",2,2), 
    ("Team K","Team L",2,0), ("Team M","Team N",1,0), 
    ("Team O","Team P",0,1), ("Team Q","Team R",0,0), 
    ("Team S","Team T",3,1), ("Team U","Team V",2,3), 
    ("Team X","Team Z",2,2), ("Team W","Team Y",1,5)]))

print(check_results("XX121X221X122", [("Team A","Team B",0,0),
    ("Team C","Team D",2,2), ("Team E","Team F",0,0), 
    ("Team G","Team H",1,1), ("Team I","Team J",1,1), 
    ("Team K","Team L",0,0), ("Team M","Team N",2,2), 
    ("Team O","Team P",0,0), ("Team Q","Team R",0,0), 
    ("Team S","Team T",1,1), ("Team U","Team V",3,3), 
    ("Team X","Team Z",2,2), ("Team W","Team Y",1,1)]))

print(check_results("1212112212122", [("Team A","Team B",0,0),
    ("Team C","Team D",2,2), ("Team E","Team F",0,0), 
    ("Team G","Team H",1,1), ("Team I","Team J",1,1), 
    ("Team K","Team L",0,0), ("Team M","Team N",2,2), 
    ("Team O","Team P",0,0), ("Team Q","Team R",0,0), 
    ("Team S","Team T",1,1), ("Team U","Team V",3,3), 
    ("Team X","Team Z",2,2), ("Team W","Team Y",1,1)]))

print(check_results("1X2211XX1X11X", [("Team A","Team B",1,0),
    ("Team C","Team D",1,1), ("Team E","Team F",0,2), 
    ("Team G","Team H",1,3), ("Team I","Team J",1,0), 
    ("Team K","Team L",1,0), ("Team M","Team N",3,3), 
    ("Team O","Team P",0,0), ("Team Q","Team R",1,0), 
    ("Team S","Team T",1,1), ("Team U","Team V",2,1), 
    ("Team X","Team Z",4,2), ("Team W","Team Y",1,1)]))