def dict(myd,p):
    temp=-1
    for i in range(len(p)):
        for j in range(len(myd)):
            if p[i]==myd[j]:
                if i>temp:
                    temp=j
                    continue
                else:
                    temp=-1
                    break
    if temp==-1:
        print("No")
    else:
        print("Yes")
myd="geeks for geekz"
p=['g','z']
print(dict(myd,p))