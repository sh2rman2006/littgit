# a=[123,2345,53,464,345,321,4235,3452345,45,1]
# print(*filter(lambda x:x>70,a))
#
# def od(n,s):
#     ms=0
#     for i in str(n):
#         ms+=int(i)
#     return ms
# def vt(n,s):
#     ms=1
#     for i in str(n):
#         ms*=int(i)
#     return ms
# def f(n,s):
#     if n==s:
#         return 1
#     if n>s:
#         return 0
#     return od(n,s)+vt(n,s)
# count=0
# for i in range(10,101):
#     if f(i,8):
#         count+=1
# print(count)


"""2"""
# print("a b c d")
# for a in range(2):
#     for b in range(2):
#         for c in range(2):
#             for d in range(2):
#                 if (((not a)and (not b))or (b==c)or d)==0:
#                     print(a,b,c,d)
"""5"""
# for n in range(1,100000):
#     r=bin(n)[2:]
#     if n%2==0:
#         r="1"+r+"0"
#     else:
#         r = "11" + r + "10"
#     sm=0
#     r=str(int(r,2))
#     for i in r:
#         sm+=int(i)
#
#     if sm>17:
#         print(bin(sm)[2:])
"""8"""

# from itertools import *
# a=product("012345678",repeat=5)
# b=[list(i) for i in a]
# count=0
# for i in b:
#     if i[0] not in "13570" :
#         if i[-1] != "1" and  i[-1] != "8":
#             if i.count("3")<2:
#                 count+=1
#                 print(i)
# print(count)
"""14"""
# def perevod(n,s):
#     string=''
#     while n>0:
#         string+=str(n%s)
#         n//=s
#     return string[::-1]
#
#
#
# for x in range(10000):
#     a =perevod(27 ** 7 - 3 ** 11 + 36-x,3)
#     sm=0
#     for i in str(a):
#         sm+=int(i)
#     if sm==22:
#         print(x,sm)
"""15"""
# for a in range(1,300):
#     count=0
#     for x in range(1,300):
#         if( (x%2==0)<=(not (x%5==0)))or (x+a>=90):
#             count+=1
#         if count==299:
#             print(a)
"""16"""
# def f(n):
#     if n<3:
#         return 1
#     if n>2 and n%2==0:
#         return 2*f(n-1)-f(n-2)
#     if n>2 and n%2!=0:
#         return f(n-1)-2*f(n-2) -3
# print(f(15))
# """19"""
# def f(n,s):
#     if n==3  and s>25:
#         return 1
#     if n==3 and s<26:
#         return 0
#     if n<3 and s>25:
#         return 0
#     if n%2==0:
#         if s%2==0:
#             return f(n+1, s+1) or f(n+1, s+2)
#         else:
#             return f(n+1, s+1) or f(n+1, s+2) or f(n+1, s*2)
#     else:
#         if s%2==0:
#             return f(n+1, s+1) and f(n+1, s+2)
#         else:
#             return f(n+1, s+1) and f(n+1, s+2) and f(n+1, s*2)
#
# def f1(n,s):
#     if (n==3 or n ==5)  and s>25:
#         return 1
#     if n==5 and s<26:
#         return 0
#     if n<5 and s>25:
#         return 0
#     if n%2==0:
#         if s%2==0:
#             return f1(n+1, s+1) or f1(n+1, s+2)
#         else:
#             return f1(n+1, s+1) or f1(n+1, s+2) or f1(n+1, s*2)
#     else:
#         if s%2==0:
#             return f1(n+1, s+1) and f1(n+1, s+2)
#         else:
#             return f1(n+1, s+1) and f1(n+1, s+2) and f1(n+1, s*2)
# for i in range(1,26):
#     if f(1,i):
#         print(i)
# print(1111111111111)
# for i in range(1,26):
#     if f1(1,i):
#         print(i)



"""20"""
# def f(n,s):
#     if n==2  and s>25:
#         return 1
#     if n==2 and s<26:
#         return 0
#     if n<2 and s>25:
#         return 0
#     if n%2!=0:
#         if s%2==0:
#             return f(n+1, s+1) or f(n+1, s+2)
#         else:
#             return f(n+1, s+1) or f(n+1, s+2) or f(n+1, s*2)
#     else:
#         if s%2==0:
#             return f(n+1, s+1) and f(n+1, s+2)
#         else:
#             return f(n+1, s+1) and f(n+1, s+2) and f(n+1, s*2)
#
# def f1(n,s):
#     if (n==2 or n ==4)  and s>25:
#         return 1
#     if n==4 and s<26:
#         return 0
#     if n<4 and s>25:
#         return 0
#     if n%2!=0:
#         if s%2==0:
#             return f1(n+1, s+1) or f1(n+1, s+2)
#         else:
#             return f1(n+1, s+1) or f1(n+1, s+2) or f1(n+1, s*2)
#     else:
#         if s%2==0:
#             return f1(n+1, s+1) and f1(n+1, s+2)
#         else:
#             return f1(n+1, s+1) and f1(n+1, s+2) and f1(n+1, s*2)
# a=set()
# b=set()
# for i in range(1,26):
#     if f(1,i):
#         a.add(i)
# for i in range(1,26):
#     if f1(1,i):
#         b.add(i)
# print(b-a)
"""21"""

"""победа 3 ходом внезависимости от хода вани"""
# def f(n,s):
#     if n==6 and s>25:
#         return 1
#     if n==6 and s<26:
#         return 0
#     if n<6 and s>25:
#         return 0
#     if n%2!=0:
#         if s%2==0:
#             return f(n+1, s+1) or f(n+1, s+2)
#         else:
#             return f(n + 1, s + 1) or f(n + 1, s + 2) or f(n+1,s*2)
#     else:
#         if s%2==0:
#             return f(n+1, s+1) and f(n+1, s+2)
#         else:
#             return f(n + 1, s + 1) and f(n + 1, s + 2) and f(n+1,s*2)
#
# def f2(n,s):
#     if( n==2 or n==4 )and s>25:
#         return 1
#     if n==4 and s<26:
#         return 0
#     if n<4 and s>25:
#         return 0
#     if n%2!=0:
#         if s%2==0:
#             return f(n+1, s+1) or f(n+1, s+2)
#         else:
#             return f(n + 1, s + 1) or f(n + 1, s + 2) or f(n+1,s*2)
#     else:
#         if s%2==0:
#             return f(n+1, s+1) and f(n+1, s+2)
#         else:
#             return f(n + 1, s + 1) and f(n + 1, s + 2) and f(n+1,s*2)
#
#
# for i in range(1,26):
#     if f(1,i):
#
#         print(i)
# print("11111111111111")
# for i in range(1,26):
#     if f2(1,i):
#
#         print(i)

# for i in range(113000000,114000000):
#     ch=0
#     k=""
#     if i%2==0:
#         ch-=1
#     for d in range(2,i//2+1,2):
#         if i%d==0:
#             ch+=1
#             k=k+","+str(d)
#     if ch==3:
#         print(i,k)





