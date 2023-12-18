import random
m=int(input("m-"))
b=[]
n=int(input("n-"))
def l():
    global b
    for i in range(n):
        a = "".join(["".join(random.choices("0123456789qwertyQWERTY")) for i in range(m)])
        b.append(a)
        for k in b:
            if b.count(k)==1:
                b=b
            if b.count(k)>1:
                l()
l()
print(",".join(b))








