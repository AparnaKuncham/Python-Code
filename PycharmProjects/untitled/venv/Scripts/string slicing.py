def ss(a,word):
    while len(a)>=len(word):
        if word in a:
            a=a.replace(word,"")
        else:
            #print("No")
            break
    if len(a)==0:
        s="Yes"
    else:
        s="No"
    return s
a="GEEGEEKSKS"
word="GEEKS"
print(ss(a,word))