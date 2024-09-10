class Mobile:
    discount = 50
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand
    def purchase(self):
        total = self.price - self.price * Mobile.discount / 100
        print (self.brand, "mobile with price", self.price, "is available after discount at", total)

# The value of a class attribute can be modified using the class name.

def enable_discount():
    Mobile.discount = 50

def disable_discount():
    Mobile.discount = 0

mob1=Mobile(20000, "Apple")
mob2=Mobile(30000, "Apple")
mob3=Mobile(5000, "Samsung")
enable_discount()
mob1.purchase()
mob2.purchase()
disable_discount()
mob3.purchase()
enable_discount()
