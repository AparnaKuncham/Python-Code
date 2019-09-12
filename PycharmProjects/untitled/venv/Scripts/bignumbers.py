def big(a):
    big=[]
    new_a=sorted(a)
    big.extend(new_a[-3:])
    return big
a=[345,65,34,56,768,343,56,34]
s=big(a)
print(s)