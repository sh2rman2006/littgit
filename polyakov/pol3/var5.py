"""5"""
# for n in range(1,1001):
#     r=bin(n)[2:]
#     if r.count('1')%2==0:
#         r='1'+r+'00'
#     else:
#         r='11'+r
#     if int(r,2)>=412:
#         print(n);break
"""17"""
# a=[int(i) for i in open('17-383.txt')]
# c=max([int(a[i]) for i in range(len(a)) if len(str(a[i]))==2])
#
# count=0
# mx=0
# for i in range(len(a)-1):
#     if (len(str(abs(a[i])))==2 or len(str(abs(a[i+1])))==2) and (a[i]+a[i+1])<=c:
#         count+=1
#         mx=max(mx,a[i]+a[i+1])
# print(count,mx)
"""9"""
# count=0
# for i in open('9-pol3.csv'):
#     a=list(map(int,i.split(';')))
#     rp=[int(i) for i in a if a.count(i)==2]
#     c=set(a)
#     if len(rp)==2 and len(c)==4:
#         sr=[int(i) for i in a if i!=max(a) and i!=min(a)]
#         for i in range(a.count(min(a))-1):
#             sr.append(min(a))
#         for i in range(a.count(max(a))-1):
#             sr.append(max(a))
#         if (max(a)+min(a))**2<(sum([i**2 for i in sr])):
#             count+=1
# print(count)
