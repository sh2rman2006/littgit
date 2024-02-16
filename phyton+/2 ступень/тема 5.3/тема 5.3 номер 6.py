STROKA=""
def k(n):
    global STROKA
    a="eyuoai,!;:'"
    for i in n:
        if i not in a:
            STROKA+=i
k(input("-"))
print(STROKA)


