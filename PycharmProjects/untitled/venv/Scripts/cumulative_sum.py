def cumulative(a):
    sum=0
    sum_list=[]
    for i in a:
        sum=sum+i
        sum_list.append(sum)
    return sum_list
a=[10,20,30,40,50]
s=cumulative(a)
print(s)