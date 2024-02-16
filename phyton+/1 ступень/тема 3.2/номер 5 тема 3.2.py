a=input("-")
s=0
while True:
    b=input("-")
    if a[-1]!=b[0]:
        break
    s+=1
    a=b
print("Слов в цепочке-", s+1)


