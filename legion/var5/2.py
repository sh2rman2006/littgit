"""2"""
# print("x y z w")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if ((not x)or y)and (x==(not z)) and w:
#                     print(x,y,z,w)
# 1y 2z 3x 4w
"""4"""
"""5"""
# a=[]
# for n in range(1,1001):
#     r=bin(n)[2:]
#     if n%2==0:
#         r+="00"
#     else:
#         r+="10"
#     if r.count("1")%2==0:
#         r+="0"
#     else:
#         r+="1"
#     if int(r,2) in range(130,351):
#         a.append(int(r,2))
# print(len(a))
"""7"""
# 5
"""8"""
# from itertools import *
# a=permutations("идиллия",r=7)
# b=set()
# for i in a:
#     b.add(''.join(i))
# print(len(b))
"""9"""
# count=0
# for i in open("9.var5.csv"):
#     j=i.replace(",",".")
#     a=list(map(float,j.split(";")))
#     zim=(a[12]+a[1]+a[2])/3
#     let=(a[6]+a[7]+a[8])/3
#     if zim>let:
#         print(a[0],zim,let)
#         count+=1
# print(count)
"""11"""
# Ip=3
# kp=5
# ip=4
# Il=9
# il=4
# kl=17
# Io=21
# 292
"""12"""
# for i in range(1, 100):
#     for j in range(1, 100):
#         for k in range(1, 100):
#             s = '0' + '2' * i + '4' * j + '6' * k
#             while '02' in s or '04' in s or '06' in s:
#                 if '02' in s:
#                     s = s.replace('02', '6404', 1)
#                 if '04' in s:
#                     s = s.replace('04', '2206', 1)
#                 if '06' in s:
#                     s = s.replace('06', '440', 1)
#             if s.count('2') == 30 and s.count('4') == 54 and s.count('6') == 10:
#                 print(k)
"""27"""
# a0=[]
# a1=[]
# a2=[]
# a3=[]
# a=open("27_B.txt")
# b=[int(i) for i in a]
# for i in b:
#     if i%4==0:
#         a0.append(i)
#     if i%4==1:
#         a1.append(i)
#     if i%4==2:
#         a2.append(i)
#     if i%4==3:
#         a3.append(i)
# print(max(a1)+max(a2)+max(a0)+max(a3))
# print(a0)



















































