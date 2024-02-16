class Words:
    def __init__(self):
        self.vse=[]
        self.short=[]
        self.long=[]
        self.ost=[]
    def add_word(self,x):
        self.vse+=x.split()
        self.vse=list(set(self.vse))
        dl=list(map(len , self.vse))
        self.short=list(filter(lambda t:len(t)==min(dl), self.vse))
        self.long=list(filter(lambda t:len(t)==max(dl), self.vse))
        self.ost=list(filter(lambda t:len(t)<max(dl) and len(t)>min(dl), self.vse))
    def shortest_words(self):
        return self.short
    def longest_words(self):
        return self.long
    def prn_words(self):
        return self.ost
poisk = Words()
poisk.add_word('hello')
poisk.add_word('abc')
poisk.add_word('world')
poisk.add_word('def')
poisk.add_word('asdf')
poisk.add_word('qwert')
poisk.add_word('hello abc world')
poisk.add_word('def asdf qwert')
print(poisk.shortest_words())
print(poisk.longest_words())
print(poisk.prn_words())
