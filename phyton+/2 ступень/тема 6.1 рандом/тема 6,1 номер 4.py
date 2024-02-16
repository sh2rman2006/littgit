import random
a="".join(["".join(random.choices("0123456789qwertyuiopasdfgQWERTYUIOPASDFG"))for i in range(random.randint(6,11))])
s=""
for i in a:
    if i in "0123456789":
        s+="a"
    if i in "qwertyuiopasdfg":
        s+="b"
    if i in "QWERTYUIOPASDFG":
        s += "c"
if s.count("a")>0 and s.count("b")>0 and s.count("c")>0:
    print(a)


