# for i in range(2,17):
#     m=0
#     count=0
#     for d in range(2,int(i**0.5)+1):
#         if i%d==0:
#             m=m+d+i//d
#     if i**0.5%1==0:
#         m-=int(i**0.5)
#     print(i,m)


for i in range(2,17):
    m=0
    count=0
    for d in range(2,int(i**0.5)+1):
        if i%d==0:
            m=m+d+i//d
    if i**0.5%1==0:
        m-=int(i**0.5)
    ostat=m%100000
    if m>0:
        for ostdel in range(2,int(ostat**0.5)+1):
            if ostat%ostdel==0:
                break
            if ostat**0.5%1==0:
                break
        else:
            print(i,m)

        # for ostdel in range(2,int(ostat**0.5)+1):
        #     if ostat%ostdel==0:
        #         count+=2
        #     if ostat**0.5%1==0:
        #         count+=1
        #     if count>0:
        #         break
        # else:
        #     print(i,m)
print(2%100000)