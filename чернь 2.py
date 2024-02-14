# from itertools import *
# count=0
# b=[list(i) for i in product('АЯНОКОДЖИ',repeat=6)]
# sp='АЯНОКОДЖИ'
# gl='АЯОИ'
# for i in b:
#     if i.count('А')==1 and i.count('О')==2 and i.count('И')==1 and i.count('Я')==1:
#         print(i)
#         sm=[]
#         for k in i:
#             if k in gl:
#                 sm.append(sp.index(k)+1)
#         sm=sum(sm)
#         print(i,sm)
#         if sm==15:
#             count+=1
# print(count)