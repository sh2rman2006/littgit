def  middle(val):
    if len(val)==0:
        return "Вы ошиблись"
    else:
        l=len(val)
        m=max(val)
        mi=min(val)
        sr=sum(val)/len(val)
        return "максимум-", m,"минимум-", mi, "длина-", l, "среднее-", sr
print(middle([int(k) for k in input("-").split()]))





