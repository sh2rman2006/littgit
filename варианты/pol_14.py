"""5"""
# def perevod(n,s):
#     string=''
#     while n>0:
#         string+=str(n%s)
#         n//=s
#     return string[::-1]
#
# for n in range(10,1001):
#     r=perevod(n,3)
#     if (r.count('0')+r.count('2'))>r.count('1'):
#         r='22'+r
#     else:
#         r='11'+r
#     if int(r,3)>100:
#         print(int(r,3))
#         break
"""8"""
# from itertools import *
# b=[''.join(i) for i in permutations("БИТКОИН",r=len("БИТКОИН"))]
# c=set(b)
# print(len(c))
"""9"""
# count=0
# for i in open('9_pol14.csv'):
#     a=list(map(int,i.split(";")))
#     c=set(a)
#     if a.count(min(a))==1 and len(c)<6:
#         sm=max(a)+min(a)
#         sr=[i for i in a if i!=max(a) and i!=min(a)]
#         for k in range(a.count(max(a))-1):
#             sr.append(max(a))
#         sr=sum(sr)/4
#         if sm < 2 * sr:
#             count += 1
# print(count)
"""17"""
# b=[int(i) for i in open('17_pol14.txt')]
# mx1=100000000000
# for i in b:
#     if len(str(i))==3 and str(i)==str(i)[::-1]:
#         mx1=min(mx1,i)
# print(mx1)
# mx=0
# count=0
# for i in range(len(b)-1):
#     if (len(str(b[i]))==4 and  len(str(b[i+1]))!=4) or (len(str(b[i]))!=4 and  len(str(b[i+1]))==4):
#         sm=b[i]**2+b[i+1]**2
#         if sm%mx1==0:
#             count+=1
#             mx=max(mx,sm)
# print(mx,count)






