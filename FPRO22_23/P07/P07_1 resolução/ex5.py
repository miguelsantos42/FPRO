def check_results(bet, results):
    hits = 0

    for i in range(len(bet)):
        if bet[i] == '1' and results[i][2] > results[i][3]:
            hits += 1
        elif bet[i] == '2' and results[i][2] < results[i][3]:
            hits += 1
        elif bet[i] == 'X' and results[i][2] == results[i][3]:
            hits += 1

    return hits


print(check_results("XX121X221X122", [("Team A","Team B",0,0),
    ("Team C","Team D",2,1), ("Team E","Team F",0,4), 
    ("Team G","Team H",1,1), ("Team I","Team J",2,2), 
    ("Team K","Team L",2,0), ("Team M","Team N",1,0), 
    ("Team O","Team P",0,1), ("Team Q","Team R",0,0), 
    ("Team S","Team T",3,1), ("Team U","Team V",2,3), 
    ("Team X","Team Z",2,2), ("Team W","Team Y",1,5)]))