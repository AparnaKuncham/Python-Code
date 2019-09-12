def ar_rotate(array):
    mid=int(len(array)/2)
    for i in range(mid):
        array[i],array[-1-i]=array[-1-i],array[i]
    return array
array=[435,234,546,65,345,234]
s=ar_rotate(array)
print(s)