'''
def fib(n):
    a,b=0,1
    for i in range(n-1):
        result=a
        a,b=b,a+b
    return a
m=int(input("Enter any number"))
s=fib(m)
print(s)
'''
import math as ma
def fib(n):
    n=5*n*n+4
    m=5*n*n-4
    s=int(ma.sqrt(n))
    t = int(ma.sqrt(m))
    if n==s*s or m==t*t:
        print("Yes")
    else:
        print("No")
m=int(input())
s=fib(m)
print(s)