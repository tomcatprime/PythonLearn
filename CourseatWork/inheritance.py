class Phone:
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")

    def return_phone(self):
        print("Returning a phone")

#In order to access the private attributes of the parent class, getter and setter method should be defined in the parent class as below:
    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price=price
# To create an inheritance relationship between the classes, mention the name of the parent class in brackets as shown:

class FeaturePhone(Phone):
    pass

# When the child has a method with the same name as that of the parent, it is said be overridden on the parent’s method. T
# This is called as Method Overriding. Method overriding is also called as Polymorphism.
class SmartPhone(Phone):
    def __init__(self, price, brand, camera, os, ram):
        # To access the parent class constructor  super() can be used.
        super().__init__(price, brand, camera)
        self.os = os
        self.ram = ram
        print("Inside SmartPhone constructor")
    def check(self):
        print(self.get_price())
    def buy(self):
        print("Buying a smartphone.")
        super().buy()
    def get_os(self):
        print(self.os)
FeaturePhone(1000,"Apple", "64px").buy()

# Since the SmartPhone class is inheriting the Phone class, the SmartPhone class inherits the constructor of the Phone class.
s1=SmartPhone(2000, "Android", "48px", "Android", 16)
print(s1.os)
print(s1.ram)
s1.buy()
s1.get_os()