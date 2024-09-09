class Mobile1:
    def __init__(self, brand, price):
        print("Inside constructor")
        self.brand = brand
        self.price = price


mob1=Mobile1("Apple", 20000)
print("Mobile 1 has brand", mob1.brand, "and price", mob1.price)
mob2=Mobile1("Samsung",3000)
print("Mobile 2 has brand", mob2.brand, "and price", mob2.price)


# mob3=Mobile(10000,'Samsung','Android')
# print("Mobile 3 has brand", mob3.brand, "and price", mob3.price)

mob4=Mobile1(10000,'Samsung')
print("Mobile 4 has brand", mob4.brand, "and price", mob4.price)


# destructor

# class Product:
#     def __init__(self,price,brand):
#         self.price=price
#         self.brand=brand
#     def __del__(self):
#         print('Deleting the object')
# p1=Product(10000,'Apple')

# p2=Product(7000,'Samsung')



# class Mobile:
#     def __init__(self):
#         print("Inside constructor")
#     def purchase (self):
#         print("Purchasing a mobile")
# mob1=Mobile()
# mob1.purchase() #Inbound method invocation, We need not pass the value for self.
# Mobile.purchase(mob1) #Outbound method invocation, We have to pass the object as the value of self.




class Mobile:
    def __init__(self, brand, price):
        print("Inside constructor")
        self.brand = brand
        self.price = price

    def purchase(self):
        self.compute(self.price, 5)
        print("Purchasing a mobile")
        print("This mobile has brand", self.brand, "and price", self.total_price, "----", "Price without tax is ", self.price, "the discount is ", self.deals, "the tax is ", self.tax)

    def compute(self, price, discount):
        self.deals = price * discount / 100
        self.tax = price * 0.03
        self.total_price = self.price + self.tax - self.deals


print("Mobile-1")
mob1=Mobile("Apple", 20000)
mob1.purchase()
print("Mobile-2")
mob2=Mobile("Samsung",3000)
mob2.purchase()
