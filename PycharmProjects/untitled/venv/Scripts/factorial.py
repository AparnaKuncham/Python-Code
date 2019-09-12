###Program to print factorial of a number
'''
n=int(input("Enter any number"))
fact=1
if n==0 or n==1:
    print(fact)
elif n>1:
    while n!=0:
        fact=fact*n
        n=n-1
    print(fact)
else:
    while n!=0:
        fact=fact*n
        n=n+1
    print(fact)



n=int(input("Enter any number"))
fact=1
if n!=0 or n!=1:
    while n!=0:
        if n<0:
            fact = fact * n
            n = n + 1
#print(fact)
        elif n>=1:
            fact=fact*n
            n=n-1
    print(fact)
    #break
'''
fact=1
def fact(n):
    if n>0:
        return fact*fact(n-1)
c=fact(5)
print(c)

