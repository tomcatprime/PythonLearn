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

class SmartPhone(Phone):
    def check(self):
        print(self.get_price())

FeaturePhone(1000,"Apple", "64px").buy()

# Since the SmartPhone class is inheriting the Phone class, the SmartPhone class inherits the constructor of the Phone class.
s1=SmartPhone(2000, "Samsung", "108px")
s1.buy()
s1.return_phone()
s1.check()