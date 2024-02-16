class Vklad:
    def __init__(self, n):
        self.n=n
    def _sroch__vklad(self,s , k=0):
        v=self.n
        a=self.n*(s/100)
        for i in range(k):
            v+=a
        return v
    def _bonus__vklad(self,s , k=0):
        v=self.n
        for i in range(k):
            a = v * (s / 100)
            v+=a
        return v
    def reshenie(self, s , k , l , p):
        a=self._sroch__vklad(s,k)
        b=self._bonus__vklad(l,p)
        print(a)
        print(b)

        if a>b:
            print("Срочный вклад лучше!!!")
        if b>a:
            print("бонусный вклад лучше!!!")
        if a==b:
            print(" вклады одинаво выгодны!!!")

r=Vklad(100)
r.reshenie(int(input("'срочный'проценты-")),int(input("'срочный'на сколько лет-")),int(input("'бонусный'проценты-")),
           int(input("'бонусный'на сколько лет-")))


