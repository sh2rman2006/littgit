a=(("Валера","17",4,"Омск"),("Серёжа","20",5,"Краснодар"),("Кирилл","18",2,"Михайловск"),
   ("Савелий","16",5,"Ставрополь"),("Илья","20",3,"Москва"),("Магомед","21",4,"Саратов"),
   ("Владислав","23",3,"Сызрань"))
sr=0
sp=[]
for i in a:
   sr+=i[2]
sr/=len(a)
for k in a:
   if k[2]>=sr:
      sp.append(k[0])
print("Ученики"+", ".join(sp)+" в этом семестре хорошо учатся!")




