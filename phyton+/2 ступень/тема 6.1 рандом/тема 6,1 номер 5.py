import random
m=int(input("m-"))
for _ in range(int(input("n-"))):
    print("".join(["".join(random.choices("0123456789qwertyQWERTY")) for i in range(m)]))



