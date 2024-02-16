class Human:
    def __init__(self,name= 'No name',age=0):
        self.name=name
        self.age=age
        self._money =0
        self._house=""
    def info(self):
        print("имя-",self.name )
        print("возраст-", self.age)
        print("на счету",self._money)
        print("дом-",self._house)
        if self._house:
            print("дом(кв.м):",self._house.area)
    def _deal(self, n="размер" ,s=0):
        self._money-=s
        self._house=n
    def money(self,n=0):
        self._money+=n
    def buy_house(self,n,sk):
        if self._money<n.price-sk:
            print("денег на счету не достаточно!")
            return False
        else:
            self._deal(n, n.price-sk)
            print("куплено!")
            return True
class House:
    def __init__(self, area, price):
        self.area=area
        self.price=price
    def final_price(self, sk):
        return self.price-sk
class SmallHouse(House):
    def __init__(self, price):
        super(SmallHouse,self).__init__(40, price)

alexander = Human('Sasha', 27)
alexander.info()
small_house = SmallHouse(8500)
alexander.buy_house(small_house, 5)
alexander.money(5000)
alexander.buy_house(small_house, 5)
alexander.money(20000)
alexander.buy_house(small_house, 5)
alexander.info()
