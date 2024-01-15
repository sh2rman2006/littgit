# for i in range(1,10**9):
#     count=0
#     for d in range(2,int(i**0.5)):
#         if i%d==0:
#             count+=2
#     if i**0.5%1==0:
#         count+=1
#     if count < 125:
#         continue
#     elif len(str(count))==3 and count**(1/3)%1==0:
#         print(i)


for i in range(1273547,1273547*5):
    m=0
    count=0
    for d in range(2,int(i**0.5)+1):
        if i%d==0:
            m=m+d+i//d
    if i**0.5%1==0:
        m-=int(i**0.5)
    ost=m%100000
    for ostdel in range(2,int(i**0.5)):
        if i%ostdel==0:
            count+=2
        if ost**0.5%1==0:
            count+=1


