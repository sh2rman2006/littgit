#1 переменная
"""for a in range(1,300):
    count=0
    for x in range(1,300):
        if ((x & 29) !=0) <=(((x & 17)==0)<=((x&a)!=0)):
            count+=1
    if count==299:
        print(a)"""
#с 2 переменными
"""for a in range(1,300):
    count=0
    for x in range(1,300):
        for y in range(1,300):
            if ((x<=9)<=(x**2<=a))and ((y**2<=a)<=(y<=9)):
                count+=1
    if count==299**2:
        print(a)"""
# с функцией ДЕЛ:
"""for a in range(1,300):
    count=0
    for x in range(1, 300):
        if (x%a!=0)<=((x%6==0)<=(x%4!=0)):
            count+=1
    if count==299:
        print(a)"""
#36870
"""for a in range(1,300):
    count=0
    for x in range(1,300):
        if ((x&49)==0)<=(((x&28)!=0)<=((x&a)!=0)):
            count+=1
        if count==299:
            print(a)"""

# for a in range(1,300):
#     count=0
#     for x in range(1,300):
#         if( (x%2==0)<=(not (x%5==0)))or (x+a>=90):
#             count+=1
#         if count==299:
#             print(a)


