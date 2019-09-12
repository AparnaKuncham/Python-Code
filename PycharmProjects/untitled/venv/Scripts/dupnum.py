import math
def dupnum(a):
    dupnum=[]
    for i in a:
        if a.count(i)>1:
            dupnum.append(i)
    return dupnum
a=[34,23,45,34,234,67,34,56,345,54]
s=dupnum(a)
print(s)