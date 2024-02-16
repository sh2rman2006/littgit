class Table_1:
    def __init__(self, x, y):
        self.base=[]
        for i in range(x):
            d=[0]*y
            self.base.append(d)
        print(self.base)
    def setting(self,x,y):
        self.base[x][y]=int(input("-"))
    def getting(self,x,y):
        return self.base[x][y]
    def rows(self):
        return len(self.base)
    def cols(self):
        return len(self.base[0])
class Table_2:
    def __init__(self, x, y):
        self.base=[]
        for i in range(x):
            self.base.append([])
            for k in range(y):
                self.base[i].append(int(input("-")))
        print(self.base)
    def setting(self,x,y):
        self.base[x][y]=int(input("-"))
    def getting(self,x,y):
        return self.base[x][y]
    def rows(self):
        return len(self.base)
    def cols(self):
        return len(self.base[0])

def print_table(n):
    if n==table1:
        for i in range(table1.rows()):
            for k in range(table1.cols()):
                print(table1.getting(i,k), end=" "*(5-len(str(table1.getting(i,k)))))
            print()
    if n==table2:
        for i in range(table2.rows()):
            for k in range(table2.cols()):
                print(table2.getting(i,k), end=" "*(5-len(str(table2.getting(i,k)))))
            print()
table1 = Table_1(3, 5)
table1.setting(0, 1)
table1.setting(1, 2)
table1.setting(2, 3)
table2 = Table_2(5, 5)
print_table(table1)
print_table(table2)

