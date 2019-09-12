
def arms(n):
    count=0
    m,N=n,n
    while m>0:
        m=int(m/10)
        count+=1
    #return count
    sum=0
    while n>0:
        temp=n%10
        sum+=temp**count
        n=int(n/10)
    return sum


n=int(input("Please neter number"))
s=arms(n)
if s==n:
    print('Yes')
else:
    print('No')
#print(s)