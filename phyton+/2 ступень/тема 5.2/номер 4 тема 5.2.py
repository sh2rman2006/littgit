def password(phrase):
    if len(phrase)<8:
        return "Пароль короткий!!!"
    a=["0",'1','2','3','4','5','6','7','8','9',"q","w",'e','r','t','y',"Q","W",'E','R','T','Y']
    b=[]
    for k in phrase:
        if k not in a:
            return "Недопустимый пароль"
        if k in a[:10]:
            b.append("c")
        if k in a[10:16]:
            b.append("b")
        if k in a[::]:
            b.append("B")
        if ("c" not in b)and("b" not in b)and("B" not in b):
            return "Ненадежный пароль"
    return "пароль верный!!!"

print(password(input("-")))







