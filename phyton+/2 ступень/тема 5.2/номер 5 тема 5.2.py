def fun(word):
    a={"1":"сто",'2':"двести",'3':"триста",'4':"четыреста",'5':"пятьсот",'6':"шестьсот",'7':"семьсот",'8':"восемьсот",'9':"девятьсот"}
    b={'1':"Десять",'2':"двадцать",'3':"тридцать",'4':"сорок",'5':"пятьдесят",'6':"шестьдесят",'7':"семьдесят",'8':"восемьдесят",'9':"девяносто"}
    c={'1':"один",'2':"два",'3':"три",'4':"четыре",'5':"пять",'6':"шесть",'7':"семь",'8':"восемь",'9':"девять"}
    if len(word)==3:
        for i in word[0]:
            for k in word[1]:
                for n in word[2]:
                    return a[i],b[k],c[n]
    if len(word)==2:
        for k in word[0]:
            for n in word[1]:
                return b[k], c[n]
    if len(word)==1:
            for n in word[0]:
                return c[n]
print(fun(input("-")))





