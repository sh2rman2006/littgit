file=open('24statgr.txt').readline()
mx=0
for i in range(len(file)):
    if file[i] in 'ab'.upper():
        ca=cb=0
        count=1
        if file[i]=="A":
            ca+=1
        else:
            cb+=1
        for k in range(i+1,len(file)):
            if ca==3 or cb==3:
                mx=max(mx,count)
                break
            if file[k]=='A':
                ca+=1
                count+=1
            if file[k]=='B':
                cb+=1
                count+=1
            if file[k]!='A' and file[k]!='B':
                count+=1
        else:
            mx=max(mx,count)
print(mx)

