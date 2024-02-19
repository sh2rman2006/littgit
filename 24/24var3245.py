file=open('24var3208974.txt').readline()
mx=-100000
for i in range(len(file)):
    if file[i]=='A':
        ca=0
        ln=0
        for k in range(i+1,len(file)):
            if ca==3:
                mx=max(mx,ln)
                break
            if file[k]=='A':
                ca+=1
                ln+=1
            else:
                ln+=1
print(mx)