for x in range(8):
    a=(2*8**5+5*8**4+6*8**3+7*8**2+x*8**1+3*8**0)+(1*8**3+x*8**2+2*8**1+4*8**0)
    if a%7==0:
        print(a/7)