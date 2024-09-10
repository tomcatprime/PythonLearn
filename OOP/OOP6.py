#hardcoded discount 50% for all mobiles

class Mobile1:
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand
        self.discount = 50
    def purchase(self):
        total = self.price - self.price * self.discount / 100
        print (self.brand, "mobile with price", self.price, "is available after discount at", total)
mob1=Mobile1(20000, "Apple")
mob2=Mobile1(30000, "Apple")
mob3=Mobile1(5000, "Samsung")
mob1.purchase()
mob2.purchase()

#programmatically enabled and disabled discountclass Mobile:
print("####################################################################")
class Mobile:
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand
        self.discount = 0
    def purchase(self):
        total = self.price - self.price * self.discount / 100
        print (self.brand, "mobile with price", self.price, "is available after discount at", total)
def enable_discount(list_of_mobiles):
    for mobile in list_of_mobiles:
        mobile.discount=50
def disable_discount(list_of_mobiles):
    for mobile in list_of_mobiles:
        mobile.discount=0
mob1=Mobile(20000, "Apple")
mob2=Mobile(30000, "Apple")
mob3=Mobile(5000, "Samsung")
mob4=Mobile(6000, "Samsung")
list_of_mobiles=[mob1,mob2,mob3,mob4]
mob1.purchase()
enable_discount(list_of_mobiles)
print("Discount enabled")
mob1.purchase()
mob2.purchase()
mob3.purchase()
disable_discount(list_of_mobiles)
print("Discount disabled")
mob4.purchase()

