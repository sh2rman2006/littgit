# def f(n,k):
#     if n==3 and k>83:
#         return 1
#     if n!=3 and k>83:
#         return 0
#     if n==3 and k<84:
#         return 0
#     if n%2==0 and k%2==0:
#         return f(n+1,k+1) or f(n+1,k*1.5)
#     if n%2==0 and k%2!=0:
#         return f(n+1,k+1) or f(n+1,k*2)
#     if n%2!=0 and k%2==0:
#         return f(n+1,k+1) and f(n+1,k*1.5)
#     if n%2!=0 and k%2!=0:
#         return f(n+1,k+1) and  f(n+1,k*2)
#
# for s in range(1,84):
#     if f(1,s):
#         print(s)
# """20"""
# def f(n,k):
#     if n==4 and k>83:
#         return 1
#     if n!=4 and k>83:
#         return 0
#     if n==4 and k<84:
#         return 0
#     if n%2!=0 and k%2==0:
#         return f(n+1,k+1) or f(n+1,k*1.5)
#     if n%2!=0 and k%2!=0:
#         return f(n+1,k+1) or f(n+1,k*2)
#     if n%2==0 and k%2==0:
#         return f(n+1,k+1) and f(n+1,k*1.5)
#     if n%2==0 and k%2!=0:
#         return f(n+1,k+1) and  f(n+1,k*2)
#
# for s in range(1,84):
#     if f(1,s):
#         print(s)
"""21"""
# def f(n,k):
#     if (n==3 or n==5) and k>83:
#         return 1
#     if n!=5 and k>83:
#         return 0
#     if n==5 and k<84:
#         return 0
#     if n%2==0 and k%2==0:
#         return f(n+1,k+1) or f(n+1,k*1.5)
#     if n%2==0 and k%2!=0:
#         return f(n+1,k+1) or f(n+1,k*2)
#     if n%2!=0 and k%2==0:
#         return f(n+1,k+1) and f(n+1,k*1.5)
#     if n%2!=0 and k%2!=0:
#         return f(n+1,k+1) and f(n+1,k*2)
#
# a=set()
# for s in range(1,84):
#     if f(1,s):
#         a.add(s)
#         print(s)
# print('//////')
#
#
# def f(n,k):
#     if n==3 and k>83:
#         return 1
#     if n!=3 and k>83:
#         return 0
#     if n==3 and k<84:
#         return 0
#     if n%2==0 and k%2==0:
#         return f(n+1,k+1) or f(n+1,k*1.5)
#     if n%2==0 and k%2!=0:
#         return f(n+1,k+1) or f(n+1,k*2)
#     if n%2!=0 and k%2==0:
#         return f(n+1,k+1) and f(n+1,k*1.5)
#     if n%2!=0 and k%2!=0:
#         return f(n+1,k+1) and  f(n+1,k*2)
#
# b=set()
# for s in range(1,84):
#     if f(1,s):
#         b.add(s)
#         print(s)
# print(a-b)
"""19"""
# def f(n,k):
#     if n==3 and k>110:
#         return 1
#     if n==3 and k<111:
#         return 0
#     if n!=3 and k>110:
#         return 0
#     if n%2==0:
#         return f(n+1,k+1) or f(n+1,k+3) or f(n+1,k*4)
#     else:
#         return f(n+1,k+1) and f(n+1,k+3) and f(n+1,k*4)
#
# for s in range(1,111):
#     if f(1,s):
#         print(s)
"""20"""
# def f(n,k):
#     if n==4 and k>110:
#         return 1
#     if n==4 and k<111:
#         return 0
#     if n!=4 and k>110:
#         return 0
#     if n%2!=0:
#         return f(n+1,k+1) or f(n+1,k+3) or f(n+1,k*4)
#     else:
#         return f(n+1,k+1) and f(n+1,k+3) and f(n+1,k*4)
# for s in range(1,111):
#     if f(1,s):
#         print(s)
"""21"""
# def f(n,k):
#     if (n==3 or n==5) and k>110:
#         return 1
#     if n==5 and k<111:
#         return 0
#     if n!=5 and k>110:
#         return 0
#     if n%2==0:
#         return f(n+1,k+1) or f(n+1,k+3) or f(n+1,k*4)
#     else:
#         return f(n+1,k+1) and f(n+1,k+3) and f(n+1,k*4)
#
# a=set()
# for s in range(1,111):
#     if f(1,s):
#         a.add(s)
#         print(s)
# print('/////')
#
# def f(n,k):
#     if n==3 and k>110:
#         return 1
#     if n==3 and k<111:
#         return 0
#     if n!=3 and k>110:
#         return 0
#     if n%2==0:
#         return f(n+1,k+1) or f(n+1,k+3) or f(n+1,k*4)
#     else:
#         return f(n+1,k+1) and f(n+1,k+3) and f(n+1,k*4)
#
# b=set()
# for s in range(1,111):
#     if f(1,s):
#         b.add(s)
#         print(s)
# print(a-b)


