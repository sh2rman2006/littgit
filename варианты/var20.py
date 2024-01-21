
# print("x y z w")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if ((not((x==y)or (x==w))) or z or (not(y<=w)))==0:
#                     print(x,y,z,w)

# for n in range(1,1000):
#     r=bin(n)[2:]
#     r=r.replace("0","00")
#     r=r.replace("1","11")
#     if int(r,2)>63:
#         print(int(r,2))

# from itertools import *
# a=product("1234",repeat=3)
# b=[list(i) for i in a]
# count=0
# for i in b:
#     if i.count("2")==1:
#         count+=1
# print(count)

# for n in range(1,1000):
#     a=">"+"1"*23+"2"*n+"3"*25
#     while (">1"in a) or (">2"in a) or( ">3"in a):
#         if ">1" in a:
#             a=a.replace(">1","1>")
#         if ">2" in a:
#             a=a.replace(">2",">3")
#         if ">3" in a:
#             a=a.replace(">3",">11")
#     sum=a.count("1")+a.count("2")*2+a.count("3")*3
#     count=0
#     for d in range(2,int(sum**0.5)):
#         if sum%d==0:
#             count+=2
#     if sum**0.5%1==0:
#         count+=1
#     if count==0:
#         print(n)

# for x in range(26):
#     for y in range(26):
#         a = (1 * 26 ** 4 + 3 * 26 ** 3 + y * 26 ** 2 + x * 26 ** 1 + 5 * 26 ** 0) + (
#                     2 * 26 ** 4 + 4 * 26 ** 3 + y * 26 ** 2 + 1 * 26 ** 1 + 3 * 26 ** 0)
#         if a%8!=0:
#             break
#     else:
#         a = (1 * 26 ** 4 + 3 * 26 ** 3 + 2 * 26 ** 2 + x * 26 ** 1 + 5 * 26 ** 0) + (
#                 2 * 26 ** 4 + 4 * 26 ** 3 + 2 * 26 ** 2 + 1 * 26 ** 1 + 3 * 26 ** 0)
#         print(a/8)


# for a in range(1,601):
#     count=0
#     for x in range(1,601):
#         for y in range(1,601):
#             if ((x<a)and(y<a)and(x*y>1200))==0:
#                 count+=1
#     if count==600**2:
#         print(a)

# def f(n):
#     if n==1 or n==2:
#         return 1
#     if n>2 and n%2==0:
#         return 3+f(n-1)
#     if n>2 and n%2!=0:
#         return 2*n+f(n-2)
# print(f(42))
""""""
# def kuch(n,s,s1):
#     if  n==3 and s*s1>=144:
#         return 1
#     if n==3 and s*s1<145:
#         return 0
#     if n<3 and s*s1>=144:
#         return 0
#     if n%2==0:
#         return kuch(n+1,s+1,s1) or kuch(n+1,s*2,s1) or kuch(n+1,s,s1+1) or kuch(n+1,s,s1*2)
#     else:
#         return kuch(n + 1, s + 1, s1) or kuch(n + 1, s * 2, s1) or kuch(n + 1, s, s1 + 1) or kuch(n + 1, s, s1 * 2)
#
# for s in range(1,145):
#     if kuch(1,2,s):
#         print(s)

# def kuch(n,s,s1):
#     if  n==4 and s*s1>=144:
#         return 1
#     if n==4 and s*s1<145:
#         return 0
#     if n<4 and s*s1>=144:
#         return 0
#     if n%2!=0:
#         return kuch(n+1,s+1,s1) or kuch(n+1,s*2,s1) or kuch(n+1,s,s1+1) or kuch(n+1,s,s1*2)
#     else:
#         return kuch(n + 1, s + 1, s1) and kuch(n + 1, s * 2, s1) and kuch(n + 1, s, s1 + 1) and kuch(n + 1, s, s1 * 2)
#
# for s in range(1,145):
#     if kuch(1,2,s):
#         print(s)


"""def kuch(n,s,s1):
    if  (n==3 or n==5) and s*s1>=144:
        return 1
    if n==5 and s*s1<145:
        return 0
    if n<5 and s*s1>=144:
        return 0
    if n%2==0:
        return kuch(n+1,s+1,s1) or kuch(n+1,s*2,s1) or kuch(n+1,s,s1+1) or kuch(n+1,s,s1*2)
    else:
        return kuch(n + 1, s + 1, s1) and kuch(n + 1, s * 2, s1) and kuch(n + 1, s, s1 + 1) and kuch(n + 1, s, s1 * 2)
a=set()
for s in range(1,145):
    if kuch(1,2,s):
        a.add(s)
        print(s)

print("///////")
def kuch(n,s,s1):
    if  n==3 and s*s1>=144:
        return 1
    if n==3 and s*s1<145:
        return 0
    if n<3 and s*s1>=144:
        return 0
    if n%2==0:
        return kuch(n+1,s+1,s1) or kuch(n+1,s*2,s1) or kuch(n+1,s,s1+1) or kuch(n+1,s,s1*2)
    else:
        return kuch(n + 1, s + 1, s1) and kuch(n + 1, s * 2, s1) and kuch(n + 1, s, s1 + 1) and kuch(n + 1, s, s1 * 2)
b=set()
for s in range(1,145):
    if kuch(1,2,s):
        b.add(s)
        print(s)
print(a-b)"""


# def f(n,s):
#     if n==s:
#         return 1
#     if n>s:
#         return 0
#     return f(n+5,s)+f(n+4,s)+f(n*3,s)
# print(f(2,6)*f(6,30))

# counti=0
# for i in range(350001,1000000):
#     m=0
#     for d in range(2,int(i**0.5)+1):
#         if i%d==0:
#             m=i//d
#             break
#     if counti == 6:
#         break
#     if m>0:
#         for delm in range(2,int(m**0.5)+1):
#             if m%delm==0:
#                 print(i, m)
#                 counti += 1
#                 break
