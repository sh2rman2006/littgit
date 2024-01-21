a=open("24_10105.txt").readline()

male=0
for i in range(len(a)):
    if a[i]=="T":
        v = 1
        c = 0
        for k in range(i + 1, len(a)):
            if a[k] == "T":
                v += 1
            else:
                c += 1
            if v==100:
                male=max(male,v+c)
                break
print(male)





