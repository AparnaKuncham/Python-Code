def uncommon(a,b):
    list_a=a.split()
    list_b=b.split()
    uc=''
    for i in list_a:
        if i not in list_b:
            uc=uc+" "+i
    return uc
a = "apple banana mango"
b = "banana fruits mango"
print(uncommon(a,b))