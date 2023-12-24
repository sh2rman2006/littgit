a=open("24var04.txt").readline()
c=0
f=-100000

for i in range(len(a)):
   if a[i]=="A":
       v=1
       c=0
       for k in range(i+1,len(a)):
           if a[k]=="A":
               v+=1
           else:
               c+=1
           if a[k]=="E" or v>700:
               f=max(f,c+v)
               break
print(f)





