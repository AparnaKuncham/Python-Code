def str(a,k):
    for i in range(len(a)):
        if i==k:
            a=a.replace(a[i],"",1)
    return a
a="vittala"
k=int(input("enter the index element to be deleted"))
print(str(a,k))
