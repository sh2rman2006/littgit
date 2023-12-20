def perevod(n,s):
    string=''
    while n>0:
        string+=str(n%s)
        n//=s
    return string[::-1]

print(5)
def perevod(n,s):
    a=[]
    while n>0:
        a.append(str(n%s))
        n//=s
    return a[::-1]

