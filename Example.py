class Products:
    def __init__(self, name, price, rating, deal_price):
        self.name = name
        self.price = price
        self.rating = rating
        self.deal_price = deal_price

    def details(self):
        return '{} {} {} {}'.format(self.name, self.price, self.rating, self.deal_price)

    def Actual_price(self):
        self.deal_price = self.price-self.deal_price
        return self.deal_price

obj = Products("Boost", 200, 5, 50)
a = obj.details()
print(a)
b = obj.Actual_price()
print(b)