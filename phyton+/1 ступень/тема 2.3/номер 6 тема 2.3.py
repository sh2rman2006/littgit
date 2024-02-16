a=1
maX=a
miN=a
while a!=0:
    a=int(input("Введите число-"))
    if a==0:
        break
    if maX<a:
        maX=a
    if miN>a:
        miN=a
print("Max=",maX)
print("Min=",miN)



