def academy_awards(alist):

    dici = {}

    for i in alist:
        if i[1] not in dici:
            dici[i[1]] = 1
        else:
            dici[i[1]] += 1
    
    return dici

print(academy_awards([('Best Picture', 'Moonlight'), ('Best Director', 'La La Land'), ('Best Actor', 'Manchester by the Sea'), ('Best Actress', 'La La Land'), ('Best Supporting Actor', 'Moonlight'), ('Best Supporting Actress', 'Fences'), ('Best Original Screenplay', 'Manchester by the Sea'), ('Best Original Score', 'La La Land')]))
