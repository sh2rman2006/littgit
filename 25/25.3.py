import fnmatch
for i in range(0,10**10,2024):
    if fnmatch.fnmatch(str(i),"3?2258*4"):
        print(i)