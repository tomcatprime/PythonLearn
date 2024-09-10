# class methods can be accessed directly by using the class name, even without creating objects.


class Mobile:
    __discount = 50
    def __init__(self, price, brand, cust_type):
        self.price = price
        self.brand = brand
        self.cust_type = cust_type
    def purchase(self):
        calculated_tax = Mobile.calculate_tax(self.cust_type)
        print("Tax to be paid:", calculated_tax)
        total = self.price - self.price * Mobile.__discount / 100
        print (self.brand, "mobile with price", self.price, "is available after discount at", total)
    @classmethod
    def enable_discount(cls):
        cls.set_discount(50)
    @classmethod
    def disable_discount(cls):
        cls.set_discount(0)
    @classmethod
    def get_discount(cls):
        return cls.__discount
    @classmethod
    def set_discount(cls, discount):
        cls.__discount = discount


# Sometimes, in a class, a method may be defined that neither accesses the class attributes nor the instance attributes. 
# These methods are generic utility functions defined within the scope of a class. Such methods are called static methods. 
# Just like class methods, static methods do not need an object to invoke them. They are accessed using the class name.
    @staticmethod
    def calculate_tax(cust_type):
        if(cust_type=='member'):
            return 0.10
        else:
            return 0.20


print('Tax percent to be paid by members:',Mobile.calculate_tax('member'), "%")
print('Tax percent to be paid by non-members:',Mobile.calculate_tax('non-member'), "%")


mob1=Mobile(20000, "Apple", "member")
mob2=Mobile(30000, "Apple", "non-member")
mob3=Mobile(5000, "Samsung", "member")
Mobile.disable_discount()
mob1.purchase()
Mobile.enable_discount()
mob2.purchase()
Mobile.disable_discount()
mob3.purchase()
Mobile.enable_discount()
print(Mobile.get_discount())

