"""a"""
# k=81
# n=790
# a=[int(i) for i in open('27-A_keglya.txt')]
# ind=a.index(max(a))#узнал что больше a[ind+2*k]
# mx=0
# for i in range(len(a)-2*k):
#     if i!=ind and (i+2*k)!=ind:
#         mx=max(mx, max(a[i]+a[i+2*k]+a[ind],a[i]+a[ind]+a[ind+2*k]))
# print(mx)
"""b"""
k=73257
# n=997506
#
# a=[int(i) for i in open('27-b_keglya.txt')]
# ind=a.index(max(a))#узнал что больше a[ind-2*k]
# mx=0
# for i in range(len(a)-2*k):
#     if i!=ind and (i+2*k)!=ind:
#         mx=max(mx, max(a[i]+a[i+2*k]+a[ind],a[i]+a[ind]+a[ind-2*k]))
# print(mx)