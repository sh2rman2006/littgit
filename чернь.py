file="23A47A11A25A28A"
ch = [str(i) for i in range(10)]
sim = 'AEIQUY'
count = 0
maxc = 0

def ysl(i,b):
    i += 3
    if ((file[i] in ch) and (file[i+1] in ch)) and (file[i+2] in sim):
        if int(file[i] + file[i+1])%2 != 0:
            b += 1
            return ysl(i,b)
        else:
            return b
    else:
        return b
print(ysl(0,1))