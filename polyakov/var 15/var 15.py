"""5"""
# def perevod(n,s):
#     string=''
#     while n>0:
#         string+=str(n%s)
#         n//=s
#     return string[::-1]
#
# for n in range(11,1001):
#     r=perevod(n,3)
#     if sum(map(int,r))%3==0:
#         r='20'+r
#     else:
#         r='10'+r
#     if int(r,3)<100:
#         print(n)
"""15"""
for x in [k*0.25 for k in range(-10000,10000)]:
    a=0
    b=70<=x<=80
    f= x%12==0 and b and x%a!=0
    if f!=1:
        print(x)