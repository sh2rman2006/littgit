def perevod(n,s):
    string=""
    while n>0:
        string+=str(n%s)
        n//=s
    return string[::-1]



"""b=[]
for x in range(13):
    for y in range(13):
        a=(8*13**4+x*13**3+7*13**2+8*13**1+y*13**0)+(7*18**4+9*18**3+x*18**2+y*18**1+7*18**0)
        if a%9==0:
            b.append(a//9)
print(min(b))"""


