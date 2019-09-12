def wordlen(a,k):
    output=''
    word = ""
    for letter in a:
        if letter==" ":
            if len(word)>=k:
                output=output+" "+word
            word=""
        else:
            word=word+letter
    return output
a="hello geeks for geeks is computer science portal f ljdgf kgljspg;txrmd bfx;mdmlx"
k=4
print(wordlen(a,k))
