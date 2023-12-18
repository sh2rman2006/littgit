class Roman:
    def __init__(self, x=""):
        self._x=x
        self._rim=(("M",1000),("D",500),("C",100),("L",50),("X",10),("V",5),("I",1))
        self._dec=(("I",  1),("IV", 4),("V",  5),("IX", 9),("X",  10),("XL", 40),("L",  50),("XC", 90),("C",  100),
                   ("CD", 400),("D",  500),("CM", 900),("M",  1000))
    def __add__(self, other):
        if type(other)==int:
            return self._to_rom(self._to_dec(self._x)+other)
        return self._to_rom(self._to_dec(self._x)+self._to_dec(other._x))
    def __sub__(self,other):
        if type(other)==int:
            return self._to_rom(self._to_dec(self._x)-other)
        return self._to_rom(self._to_dec(self._x)-self._to_dec(other._x))
    def __mul__(self, other):
        if type(other)==int:
            return self._to_rom(self._to_dec(self._x)*other)
        return self._to_rom(self._to_dec(self._x)*self._to_dec(other._x))
    def __truediv__(self, other):
        if type(other)==int:
            if other != 0:
                return self._to_rom(self._to_dec(self._x)/other)
            else:
                "деление на ноль !!"
        if other._x=="" or other._x=="0":
            return "деление на ноль !!"
        return self._to_rom(self._to_dec(self._x)/self._to_dec(other._x))


    def _to_dec(self, x):
        rez=0
        for i in self._rim:
            if i[0] in x:
                index=x.find(i[0])
                break
        for i in x[index:]:
            for k in self._rim:
                if k[0]==i:
                    rez+=k[1]
        for i in x[:index]:
            for k in self._rim:
                if k[0]==i:
                    rez+=-k[1]
        return rez

    def _to_rom(self, x):
        rez = ""
        for i in self._dec[::-1]:
            div = x // i[1]
            x %= i[1]
            if div > 0:
                rez += i[0] * div
        return rez


r1=Roman("VI")
r2=Roman("XXXV")

print(r1+r2)
