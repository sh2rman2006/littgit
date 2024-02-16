class AmericaDate:
    def __init__(self, dd, mm, gg):
        self.dd=dd
        self.mm=mm
        self.gg=gg
    def set_dd(self, dd):
        self.dd =str(dd)
        if len(self.dd)==1:
            self.dd="0"+self.dd
    def set_mm(self, mm):
        self.mm = str(mm)
        if len(self.mm) == 1:
            self.mm = "0" + self.mm
    def set_gg(self, gg):
        self.gg = str(gg)
    def get_dd(self):
        self.dd=str(self.dd)
        if len(self.dd)==1:
            self.dd="0"+self.dd
        return self.dd
    def get_mm(self):
        self.mm = str(self.mm)
        if len(self.mm) == 1:
            self.mm = "0" + self.mm
        return self.mm
    def get_gg(self):
        self.gg=str(self.gg)
        return self.gg
class EuropeDate:
    def __init__(self, dd, mm, gg):
        self.dd=dd
        self.mm=mm
        self.gg=gg
    def set_dd(self, dd):
        self.dd =str(dd)
        if len(self.dd)==1:
            self.dd="0"+self.dd
    def set_mm(self, mm):
        self.mm = str(mm)
        if len(self.mm) == 1:
            self.mm = "0" + self.mm
    def set_gg(self, gg):
        self.gg = str(gg)
    def get_dd(self):
        self.dd=str(self.dd)
        if len(self.dd)==1:
            self.dd="0"+self.dd
        return self.dd
    def get_mm(self):
        self.mm = str(self.mm)
        if len(self.mm) == 1:
            self.mm = "0" + self.mm
        return self.mm
    def get_gg(self):
        self.gg = str(self.gg)
        return self.gg
def print_date(n,k):
    if n==europe:
        return k+"("+europe.get_gg()+"."+europe.get_mm()+"."+europe.get_dd()+")"
    if n==america:
        return k + "(" + europe.get_gg() + "." + europe.get_mm() + "." + europe.get_dd() + ")"

america = AmericaDate(2000, 4, 10)

europe = EuropeDate(2000, 4, 10)

print(print_date(europe, 'en'))

print(print_date(america, "am"))

america.set_dd(25)
print(america.get_dd())
"""значение меняет,что видно в строке 71 и 72, но при выводе оно остаётся неизменным """
print(print_date(america, "am"))