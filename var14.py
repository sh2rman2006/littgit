"""16"""
# def f(n):
#     if n==1 :
#         return 1
#     if n%2==0 and n>1:
#         return n+3*f(n-1)
#     if n%2!=0 and n>1:
#         return 2+2*f(n-2)
# print(f(23))
"""19"""
# def f(n,s,s1):
#     if n==3 and s+s1>=118:
#         return 1
#     if n==3 and s+s1<118:
#         return 0
#     if n<3 and s+s1>=118:
#         return 0
#     if n%2==0:
#         return f(n+1,s+2,s1) or f(n+1,s*2,s1) or f(n+1,s,s1+2) or f(n+1,s,s1*2)
#     else:
#         return f(n+1,s+2,s1) or f(n+1,s*2,s1) or f(n+1,s,s1+2) or f(n+1,s,s1*2)
# for i in range(1,114):
#     if f(1,3,i):
#         print(i)

"""20"""
# def f(n,s,s1):
#     if n==4 and s+s1>=118:
#         return 1
#     if n==4 and s+s1<118:
#         return 0
#     if n<4 and s+s1>=118:
#         return 0
#     if n%2!=0:
#         return f(n+1,s+2,s1) or f(n+1,s*2,s1) or f(n+1,s,s1+2) or f(n+1,s,s1*2)
#     else:
#         return f(n+1,s+2,s1) and f(n+1,s*2,s1) and f(n+1,s,s1+2) and f(n+1,s,s1*2)

"""21"""

# def f(n,s,s1):
#     if (n==3 or n==5) and s+s1>=118:
#         return 1
#     if n==5 and s+s1<118:
#         return 0
#     if n<5 and s+s1>=118:
#         return 0
#     if n%2==0:
#         return f(n+1,s+2,s1) or f(n+1,s*2,s1) or f(n+1,s,s1+2) or f(n+1,s,s1*2)
#     else:
#         return f(n+1,s+2,s1) and f(n+1,s*2,s1) and f(n+1,s,s1+2) and f(n+1,s,s1*2)
# for i in range(1,114):
#     if f(1,3,i):
#         print(i)
# print("??????????????????????")
# def f(n,s,s1):
#     if n==3 and s+s1>=118:
#         return 1
#     if n==3 and s+s1<118:
#         return 0
#     if n<3 and s+s1>=118:
#         return 0
#     if n%2==0:
#         return f(n+1,s+2,s1) or f(n+1,s*2,s1) or f(n+1,s,s1+2) or f(n+1,s,s1*2)
#     else:
#         return f(n+1,s+2,s1) and f(n+1,s*2,s1) and f(n+1,s,s1+2) and f(n+1,s,s1*2)
# for i in range(1,114):
#     if f(1,3,i):
#         print(i)
"""23"""
# def f(n,s):
#     if n==s:
#         return 1
#     if n<s:
#         return 0
#     return f(n-1,s) +f(n//2,s)
# print(f(31,12)*f(12,2))



