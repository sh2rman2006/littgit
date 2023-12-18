class Calc:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def summ(self):
        print(self.x + self.y)
    def razn(self):
        print(self.x - self.y)
    def proiz(self):
        print( self.x * self.y)
    def delen(self):
        if self.y==0:
            print("деление на ноль!")
        else:
            print(self.x / self.y)
rezultl = Calc(4, 9)
rezultl.summ()
rezultl.razn()
rezultl.proiz()
rezultl.delen()





