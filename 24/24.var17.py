a=open("24var13-17.txt").readline()
ma=-1000
maxa=""
for i in range(len(a)):
    if a[i]=="Z":
        b=0
        count=0
        c=a[i]
        for k in range(i+1,len(a)):
            if a[k]=="Z":
                b+=1
                c+=a[k]
            else:
                count+=1
                c+=a[k]
            if b==3:
                # ma = max(ma, count+b)
                if count+b>ma:
                    ma=count+b
                    maxa=c
                break

print(ma)
print(maxa)