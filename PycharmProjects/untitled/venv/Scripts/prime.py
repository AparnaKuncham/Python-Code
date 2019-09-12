'''
def prime(n):
    for i in range(2,n):
        if n%i==0:
            result="Not prime"
            break
    else:
        result='Prime'
    return result
n=int(input("Enter any number"))
s=prime(n)
print(s)
'''
def prime(s,e):
    for i in range(s,e):
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                print(i)
s=int(input("ENter s"))
e=int(input("ENter e"))
s=prime(s,e)
print(s)
