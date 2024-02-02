"""9"""
# count=0
# for i in open("9.var3.csv"):
#     a=list(map(int,i.split(";")))
#     sr=[x for x in a if x!=max(a) and x!=min(a)]
#     if a.count(max(a))>1:
#         for l in range(a.count(max(a))-1):
#             sr.append(max(a))
#     if a.count(min(a))==2:
#         for l in range(a.count(min(a)) - 1):
#             sr.append(min(a))
#     sr2=2*sum(sr)
#     if (max(a)+min(a))<sr2:
#         count+=1
# print(count)
"""17"""
# a=open("17.txt")
# b=[int(i) for i in a]
# mn=min(b)
# d=[i for i in b if i%4==0]
# d=sum(d)/len(d)
# count=0
# sm=-10000000000000
# for i in range(len(b)-1):
#     if (b[i]+b[i+1])<d and (b[i]%mn==0 or b[i+1]%mn==0):
#         sm=max(sm,b[i]+b[i+1])
#         count+=1
# print(sm,count)
"""24"""
# a=open("24.txt").readline()
# mx=-100000000000
# for i in range(len(a)):
#     if a[i]=="A":
#         c=0
#         v=1
#         for k in range(i+1,len(a)):
#             if a[k]=="A":
#                 v+=1
#             else:
#                 c+=1
#             if v==3:
#                 c+=1
#                 mx=max(mx,c)
#                 break
# print(mx)
"""23"""
# def f(n,s):
#     if n==s:
#         return 1
#     if n>s:
#         return 0
#     return f(n+1,s)+f(n*3,s)
#
# print(f(1,11)*f(11,34))
"""16"""
# def f(n):
#     if n<=1:
#         return 1
#     if n==2:
#         return 2
#     if n>2 and n%3==0:
#         return 2*n-f(n//3)-f(n-1)
#     if n>2 and n%3!=0:
#         return n+f(n-2)+f(n//10)
# count=0
# for i in range(50,101):
#     if 50<f(i)<=200:
#         count+=1
# print(count)
"""15"""
# for a in range(1,1001):
#     count=0
#     for x in range(1,1001):
#         if ((x%a!=0)<=((x%27==0)<=(x%89!=0)))and (a>300):
#             count+=1
#     if count==1000:
#         print(a)













