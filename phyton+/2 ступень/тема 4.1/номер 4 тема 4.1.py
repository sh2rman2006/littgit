a=[]
s=1
for i in range(int(input("Введите количество эл.-"))):
    a.append(int(input("введите число-")))
for i in a:
    s*=i
print(sum(a),s,max(a),min(a))


