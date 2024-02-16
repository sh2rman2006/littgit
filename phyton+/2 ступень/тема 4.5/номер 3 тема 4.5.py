a=tuple(input("кортеж-").split())
el=input("элемент-")
b=0
if el not in a:
    print("нет")
else:
    if a.count(el)==1:
        b=a.index(el)
        print(a[b::])
    if a.count(el)==2:
        for i in range(len(a)):
            if a[i]==el:
                break
        for k in range(i+1, len(a)):
            if a[k]==el:
                break
        print(a[i+1:k])




