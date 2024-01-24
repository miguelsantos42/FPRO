def check_results(bet, results):
    total = 0
    for i in range(len(bet)):
        if ((bet[i] == '1') and (results[i][2] > results[i][3])):
            total = total + 1
        elif ((bet[i] == '2') and (results[i][2] < results[i][3])):
            total = total + 1
        elif ((bet[i] == 'X') and (results[i][2] == results[i][3])):
            total = total + 1
        else:
            continue
    return total


print(check_results("1X2211XX1X11X", [("Team A","Team B",1,0),
    ("Team C","Team D",1,1), ("Team E","Team F",0,2), 
    ("Team G","Team H",1,3), ("Team I","Team J",1,0), 
    ("Team K","Team L",1,0), ("Team M","Team N",3,3), 
    ("Team O","Team P",0,0), ("Team Q","Team R",1,0), 
    ("Team S","Team T",1,1), ("Team U","Team V",2,1), 
    ("Team X","Team Z",4,2), ("Team W","Team Y",1,1)]))