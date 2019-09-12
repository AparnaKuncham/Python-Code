def ls(l,n):
    for i in range(len(l)):
        if n==l[i]:
            return i
    return -1
l=[435,56,234,657,324,765]
n=765
print(ls(l,n))
