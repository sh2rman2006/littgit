NUMBER=[]
def k(n):
    for i in range(n):
        NUMBER.append((input("-")))
    for i in NUMBER:
        if NUMBER.count(i)==1:
            print(int(i), end=" ")
    if NUMBER.count("")==len(NUMBER):
        print("Вы ничего не делали!")
k(int(input("сколько чисел-")))

