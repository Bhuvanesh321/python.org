class Groceri:
    def __init__(self, g1, g2, g3, total_discount):
        self.g1 = g1
        self.g2 = g2
        self.g3 = g3
        self.total_discount = total_discount

    def G_details(self):
        return '{} {} {} {}'.format(self.g1, self.g2, self.g3, self.total_discount)

    def Price(self):
        return self.g1, self.g2 , self.g3

    def G_discounts(self):
        self.total_discount = ((self.g1+self.g2+self.g3) / (self.total_discount))
        return self.total_discount

obj = Groceri(20,30,40, 10)
a = obj.G_details()
print(a)
b = obj.G_discounts()
print(b)


