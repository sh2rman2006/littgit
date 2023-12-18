def pas():
    r="321"
    p=0
    for i in range(3):
        print("-", i+1 ,"-")
        p=input("введите пароль-")
        if p==r:
            print("пароль введен правильно!")
            break
        if p!=r:
            print("Пароль не принят!")
pas()
