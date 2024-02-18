"""a"""
# b=[int(i) for i in open('27A__lsnd.txt')]
# mx=0
# for i in range(len(b)):
#     for k in range(i+1,len(b)):
#         if (b[i]*b[k])%21==0:
#             mx=max(mx,b[i]*b[k])
# print(mx)
"""b"""
b=[int(i) for i in open('27B__asd.txt')]
mx=0
# for i in range(len(b)):
#     for k in range(i+1,len(b)):
#         if (b[i]*b[k])%21==0:
#             mx=max(mx,b[i]*b[k])
print(mx)


c=[i for i in b if i%21==0 or i%7==0 or i%3==0]
for i in range(len(c)):
    if (c[c.index(sorted(c)[i])]*max(b))%21==0:
        mx=max(c[c.index(sorted(c)[i])]*max(b),mx)
print(mx)



