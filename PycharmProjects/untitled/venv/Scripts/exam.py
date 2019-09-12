'''
sum=0
list=[-8,45,23,8,-7,34,-9]
for i in list:
    if i>0:
        sum=sum+i
print(sum)

string="-abkhflc1"
#print(string[::-1])
temp='-'
for i in range(len(string)-1,0,-1):
    temp=temp+string[i]
print(temp)

str="-abc"
#str=str.strip().split(" ")

print(str[1::][::-1])

############First method
str="geeksforgeeks"
print(str.count('eek'))
c="eek"
######333Second method
'''
str="geeksforgeekseekeek"
c='eek'
count=0
for i in range(0,len(str)):
    if str[i:len(c)+i]==c:
        count+=1
print(count)