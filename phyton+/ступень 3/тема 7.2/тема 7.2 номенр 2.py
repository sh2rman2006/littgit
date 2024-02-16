class Words:
    def __init__(self):
        self.vse=[]
        self.short=[]
        self.long=[]

    def add_stroka(self,x):
        self.vse+=x.split()
        self.vse=list(set(self.vse))
        dl=list(map(len , self.vse))
        self.short=list(filter(lambda t:len(t)==min(dl), self.vse))
        self.long=list(filter(lambda t:len(t)==max(dl), self.vse))

    def short_words(self):
        return sorted(self.short)
    def long_words(self):
        return sorted(self.long)


text = Words()

text.add_stroka('hello abc world')

text.add_stroka('def asdf qwert')

print(' '.join(text.short_words()))

print(' '.join(text.long_words()))