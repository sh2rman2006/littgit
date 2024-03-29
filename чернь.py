from itertools import *
a=[''.join(i) for i in permutations('cccckkkzz',r=len('cccckkkzz'))]
count=set()
for i in a:
    for k in range(len(i)-1):
        if i[k]+i[k+1] == 'zz' or i[k]+i[k+1] == 'cc' or i[k]+i[k+1] == 'kk':
            break
    else:
        count.add(i)
print(len(count),count)