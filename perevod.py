def perevod(n,s):
    string=''
    while n>0:
        string+=str(n%s)
        n//=s
    return string[::-1]
