import random
class Formation:
    def __init__(self,x , y):
        self.x=x
        self.y = y
    def prnt(self,z):
        if z=='rand':
            r=[]
            for i in range(self.x):
                r.append(random.randrange(-10,10))
            print(r)
        if z == 'users':
            r=[]
            for i in range(self.y):
                r.append(int(input("число-")))
            print(r)

formation = Formation(5, 9)
formation.prnt('rand')
formation.prnt('users')
