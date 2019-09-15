####Program to print n.of lines, no.of words, no.of letters present in a file
with open("sample_file","r") as f:  ##Opening file as f
    data=f.read()  ##storing file contents in a variable called data
    print(data) #printing out the data
f=open('sample_file',"r")
lcount=0
wcount=0
ccount=0
for lines in f:
    lcount+=1 ##To find no.of lines in a file
    words=lines.strip().split()  # To find no.of words in a file
    wcount+=len(words)  # To find no.of letters in a file
    for i in words:
        ccount+=len(i)
print(lcount)
print(wcount)
print(ccount)

