# kolvo = 0
# m2=[0]
# ind=0
# for i in range(2,51):
#     m = 0
#     maxdel = []
#     for d in range(2, int(i ** 0.5) + 1):
#         if i%d==0 and i**0.5!=d:
#             maxdel.append(d)
#     if len(maxdel)>0:
#         m = max(maxdel) + i // max(maxdel)
#     m2.append(m)
#     if m%10==0 and m>m2[ind]:
#         kolvo += 1
#         ind+=1
#         if kolvo < 6:
#             print(i, m)
#         else:
#             break
#     else:ind+=1



a="124456943"
print(len(a))
ma=0
for i in range(len(a)):
    if a[i]=="1":
        count=0
        for k in range(i+1,len(a)):
            if a[k]=="3":
                ma=max(count,ma)
                count=0
            else:
                count+=1
print(ma)

