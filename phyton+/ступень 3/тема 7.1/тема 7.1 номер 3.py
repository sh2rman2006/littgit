class Alphabet:
    def __init__(self, x):
        self.x=x
    def print(self):
        print(self.x)
    def add_letters(self,y):
        self.x+=y
    def letters_num(self):
        return len(self.x)
    def is_en_letter(self, t):
        return t in "QWERTYUIOPASDFqwertyuiopasdf"
alphabet = Alphabet("F")
alphabet.print()
alphabet.add_letters('A')
print(alphabet.letters_num())
alphabet.add_letters('М')
print(alphabet.is_en_letter('F'))
print(alphabet.is_en_letter('Щ'))
alphabet.print()








