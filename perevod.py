def perevod(n,s):
    string=''
    while n>0:
        string+=str(n%s)
        n//=s
    return string[::-1]


def f(n,s):
    for i in range(len(n)):
        n[i]=n[i]*s**(len(n)-1-i)
    return sum(n)
