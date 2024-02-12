from fnmatch import *
for i in range(2024,10**10,2024):
    if fnmatch(str(i),'1?2*4'):
        if i ** 0.5 % 1 == 0:
            print(i,i/2024)