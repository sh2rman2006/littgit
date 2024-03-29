def f(n,s):
    for i in range(len(n)):
        n[i]=n[i]*s**(len(n)-1-i)
    return sum(n)

""" кегэ 12731 """
for x in range(13):
    a=f([9,x,10,11],13)+f([x,4,6,12],16)-f([11,7,x],15)
    if a%14==0:
        print(a//14)
