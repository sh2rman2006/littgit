class Country:
    def __init__(self, n):
        self.name=n
class Region(Country):
    def __init__(self , n , s="край"):
        super(Region, self).__init__(n)
        self.stat=s
    def get_info(self):
        return len_obl.name, len_obl.stat


len_obl = Region("Иркутская область", "область")
print(len_obl.get_info())