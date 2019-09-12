def delnul(a):
    for i in a:
        if i==None or i=='NULL' or i==False or i==() :
            a.remove(i)
    return a
a=[23,(),324,(),343,34423,234,()]
s=delnul(a)
print(s)


'''
a=filter(None,a)
'''