'''
#####To read contents of a file######################################
with open('sample_file','r') as f:
    data=f.read()
    print(data)

########Copying contents of one file to another######################
with open('sample_file','r') as f:
    with open("abcd",'w') as f1:
        for lines in f:
            f1.write(lines)

###To read n lines of data from a file###############################3

###Method one
from itertools import islice
with open("sample_file",'r') as f:
    for lines in islice(f,4):
        print(lines,end="")

print()
#####Method 2
with open("sample_file","r") as f:
    count=0
    for lines in f:
        count+=1
        if count<5:
            print(lines,end="")

#####Program to append some text to an existing file
with open("sample_file","a") as f:
    f.write("mugulunage eh nee helu mugulu nage eh nee helu \n")
f1=open("sample_file")
print(f1.read())

####Program to print last n lines of a file######################
############Method one
from itertools import islice
with open("sample_file","r") as f:
    lcount=0
    for lines in f:
        lcount+=1
    print(lcount)
f=open("sample_file","r")
for lines in islice(f,lcount-6,lcount):
    print(lines,end="")


############Method 2
with open('sample_file',"r") as f:
    lcount=0
    for lines in f:
        lcount+=1
f=open("sample_file","r")
count=0
for lines in f:
    count+=1
    if count>(lcount-2):
        print(lines,end="")



#######Store lines of files into a list#########
####Method one
with open("sample_file","r") as f:
    list=[]
    for lines in f:
        list.append(lines)
    print(list)


######Method 2
with open("sample_file","r") as f:
    list=f.readlines()
    print(list)
    print(type(list))

########Program to find longest word in a file###########
with open("sample_file","r") as f:
    words=[]
    for lines in f:
        words.extend(lines.split())
    longest=len(words[0])
    lw=words[0]
    for i in words:
        if longest<len(i):
            lw=i
            longest=len(i)
    print(lw)
##########Words Counter
from collections import Counter
with open("sample_file","r") as f:
    words=f.read().split()
    print(Counter(words))
print(words)



###Find length of the file

import os
#with open("sample_file","r") as f:
print(os.stat("sample_file").st_size)


##Program to write a list to a file
with open("sample_file","a") as f:
    list=["\neleventh\n","twelth\n","thirteenth"]
    for i in list:
        print("\n")
        f.write(i)

'''
f=open("sample_file","r")
print(f.closed)
print(f.tell())
f.close()
print(f.closed)
