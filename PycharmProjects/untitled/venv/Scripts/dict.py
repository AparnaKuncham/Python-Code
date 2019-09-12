def diction(mydict):
    keys=[]
    values=[]
    for i in sorted(mydict.keys()):
        keys.append(i)
        values.append(mydict[i])
    return dict(zip(keys,values))
mydict={6:'fdg',54:'gfs',5:'dfs'}
print(diction(mydict))