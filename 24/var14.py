a=open("24var13-17.txt").readline()
count=0
p=0
for i in range(len(a)-1):
    if a[i]=="Z" and (a[i+1]=="Z" or a[i+1]=="Y"):
        count+=1
    elif a[i] == "Y" and (a[i + 1] == "x".upper() or a[i + 1] == "y".upper()):
        count += 1
    elif a[i]=="x".upper() and (a[i+1]=="x".upper()):
        count+=1
    else:
        p=max(p,count)
        count=0
print(p)




#     if a[i]=="z":
#         k=1
#     elif a[i]=="y":
#         k=2
#     else:
#         k=3
#     if a[i+1]=="z":
#         c=1
#     elif a[i+1]=="y":
#         c=2
#     else:
#         c=3
#     if k==c or k==(c+1):
#         count+=1
#     else: count=0
# print(count)