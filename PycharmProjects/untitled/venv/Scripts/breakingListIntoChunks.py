def breaking(a,n):
    new_list=[]
    m = 0
    for i in range(0,len(a),n):
        new_list.append(a[m:m+n])
        m=m+n
    return new_list
a=[34,23,23,23,43,56,76,456,345,76,345,65,76]
s=breaking(a,4)
print(s)
