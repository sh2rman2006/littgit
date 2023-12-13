#40740
a=open("24(4).txt").readline()
le=0
p=0
st=""
for i in range(len(a)):
    if a[i]!="A":
        st+=a[i]
        if st.count("E")>3:
            le+=1
    else:
        p=max(p,le)
        le=1
print(p)
