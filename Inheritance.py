class product:
    def __init__(self, name, price, deal_price, ratings):
        self.name = name
        self.price = price
        self.deal_price = deal_price
        self.ratings = ratings
        self.you_save = price - deal_price

    def display_product_details(self):
        print("Product:{}".format(self.name))
        print("Price: {}".format(self.price))
        print("Deal price: {}".format(self.deal_price))
        print("Ratings: {}".format(self.ratings))
        print("You saved: {}".format(self.you_save))

    def get_deal_price(self):
        return self.deal_price


class ElectronicItem(product):
    def set_warranty(self, warrantly_in_months):
        self.warranty_in_months = warranty_in_months

    def get_warranty(self):
        return self.warranty_in_months


class GroceryItem(product):
    pass


class Order:
    def __init__(self, delivery_speed, delivery_address):
        self.items_in_cart = []
        self.delivery_speed = delivery_address

    def add_item(self, product, quality):
        self.items_in_cart.append((product, quality))

    def display_order_details(self):
        for product, quality in self.items_in_cart:
            print("Quality: {}".format(quality))
            product.display_product_details()

    def display_total_bill(self):
        total_bill = 0
        for product, quality in self.items_in_cart:
            price = product.get_deal_price() * quality
            total_bill += price
        print("Total Bill:{}".format(total_bil))

    def remove_item(self, product):
        self.items_in_cart.((product))
milk = GroceryItem("Milk", 40, 25, 3.5)

tv = ElectronicItem("TV", 45000, 40000, 3.5)

order = Order("Prime Delivery", "Huderabad")

order.add_item(tv, 1)
order.add_item(milk, 2)
order.remove_item(tv)
print("+++++")
order.display_order_details()
print("+++++")
order.display_total_bill()

