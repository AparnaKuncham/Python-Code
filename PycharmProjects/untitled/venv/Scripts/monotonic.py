def mono(a):
    n=len(a)
    if a[0]>a[1]:
        for i in range(1,n):
            if a[i]>a[i-1]:
                print("not monotonic")
                break
        else:
            print("Monotonic")
    elif a[0]<a[1]:
        for i in range(1,n):
            if a[i]<a[i-1]:
                print("not monotonic")
                break
        else:
            print("Monotonic")
arr=[12,34,56,67,87,565,1056]
s=mono(arr)
print(s)

