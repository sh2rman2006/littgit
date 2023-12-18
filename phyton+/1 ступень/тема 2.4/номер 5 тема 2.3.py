m=int(input(" Введите кол. строк-"))
n=int(input(" Введите кол. столбцов-"))
for i in range(1,n+1):
    print(" номер столбца", i, end=" ")
    for h in range(1,m+1):
        print(i / h, end=" ")
    print(" ")








