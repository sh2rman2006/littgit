# sknfks=25
# mx=[]
# mn=[]
# for i in open('27_A.txt'):
#     a=list(map(int,i.split(' '*i.count(' '))))
#     mx.append(max(a))
#     mn.append(min(a))
# sm=sum(mx)
# otv=0
# for i in range(len(mx)):
#     if (sm-mx[i]+mn[i])%4==0:
#         otv=max((sm-mx[i]+mn[i]),otv)
# print(otv)

"""b"""
# mx=[]
# mn=[]
# for i in open('27_B_prob.txt'):
#     a=list(map(int,i.split(' '*i.count(' '))))
#     mx.append(max(a))
#     mn.append(min(a))
# sm=sum(mx)
# otv=0
# for i in range(len(mx)):
#     if (sm-mx[i]+mn[i])%4==0:
#         otv=max((sm-mx[i]+mn[i]),otv)
# print(otv)