def sl(a):
    max=a[0]
    sm=a[0]
    for i in range(len(a)):
        if i+1<len(a):
            if max<a[i+1]:
                sm=max
                max=a[i+1]
    return sm
a=[324,45,23,56,345,56,234,400,532]
s=sl(a)
print(s)
