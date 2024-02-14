a=(open('24_mal.txt').readline()).split("U")
mxl=0
for i in a:
    mxl=max(mxl,len(i))
sm='TVWXYZ'
for i in a:
    if len(i)==mxl:
        for k in sm:
            print(k,i.count(k))

