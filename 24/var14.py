a=open("24var13-17.txt").readline()
count=1
p=0
m=set()
for i in range(len(a)-1):
    if (a[i]=="Z" and (a[i+1]=="Y" or a[i+1]=="Z")) or (a[i]=="Y" and (a[i+1]=="Y" or a[i+1]=="X")) or (a[i]=="X" and a[i+1]=="X"):
        flag=True
    else:
        m.add(a[i]+a[+1])
        flag=False
    if flag:
        count+=1
    else:
        p=max(p,count)
        count=1
print(p)
print(m)




#     if a[i]+a[i+1]=="ZZ" or a[i]+a[i+1]=="ZY" or a[i]+a[i+1]=="YY" or a[i]+a[i+1]=="YX" or a[i]+a[i+1]=="XX":
#         flag=True
#     else:
#         m.add(a[i]+a[+1])
#         flag=False
#     if flag:
#         count+=1
#     else:
#         p=max(p,count)
#         count=1
# print(p)
# print(m)







#     if a[i]+a[i+1]=="ZZ":
#         flag=True
#     else:
#         flag=False
#     if flag:
#         count+=1
#     else:
#         p=max(p,count)
#         count=1
# print(p)