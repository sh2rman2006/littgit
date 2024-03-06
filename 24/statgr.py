# file=open('24statgr.txt').readline()
# mx=0
# for i in range(len(file)):
#     if file[i]=='A' or file[i]=='B':
#         ca=cb=0
#         if file[i]=='A':
#             ca=1
#         else:
#             cb=1
#         count=0
#         for k in range(i+1,len(file)):
#             if cb==3 or ca==3:
#                 mx=max(mx,count)
#                 break
#             if file[k]=="A":
#                 ca+=1
#                 count+=1
#             elif file[k]=='B':
#                 cb+=1
#                 count+=1
#             else:
#                 count+=1
# print(mx)



