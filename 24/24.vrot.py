from itertools import *
a=product("abcdefu".upper(),repeat=3)
sogl="BCDF"
gl="AEU"
file =open("24.vrot.txt").readline()

komb=["".join(i) for i in a if (i[0] in sogl) and (i[1] in gl) and (i[2] in sogl)]
print(komb)

count=0
maxc=0

for i in range(len(file)-2):
    if file[i]+file[i+1]+file[i+2] in komb:
        for k in range(i+1,len(file)-2):
            v=1
            if file[k]+file[k+1]+file[k+2] in komb:
                v+=1
                count+=1
            if v==2:
                maxc=max(count,maxc)
                count=2
                break
            else:
                count+=1
print(maxc)






