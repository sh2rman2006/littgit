import random

a=int(input("от-"))
b=int(input("до-"))
c=input("i/f-")
if c=="i":
    print(random.randint(a,b))
if c=="f":
    print(random.uniform(a,b))
