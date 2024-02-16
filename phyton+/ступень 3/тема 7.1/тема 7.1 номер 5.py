class Multi:
    def add_number(self,x):
        self.x=x.split()
        self.x=list(map(int, self.x))
    def prn(self,y):
        if y=='odd':
            self.x=filter(lambda t:t%2==0,self.x)
            print(*self.x)
        if y=='even':
            self.x=filter(lambda t:t%2!=0,self.x)
            print(*self.x)

numbers = Multi()
numbers.add_number('2 5 1 7 9')
numbers.prn('odd')
numbers.prn('even')
numbers.add_number('4 8 1 11 0')
numbers.prn('odd')
numbers.prn('even')



