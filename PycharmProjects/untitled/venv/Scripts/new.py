import re
test_string="sphain"
pattern='^s...n$'
res=re.findall(pattern,test_string)
if res:
    print("Yes")
else:
    print("No")
