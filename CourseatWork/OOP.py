class Mobile:
    def __init__(self, brand, price):
        print("Inside constructor")
        self.brand = brand
        self.price = price
mob1=Mobile("Apple", 20000)
print("Mobile 1 has brand", mob1.brand, "and price", mob1.price)
mob2=Mobile("Samsung",3000)
print("Mobile 2 has brand", mob2.brand, "and price", mob2.price)


class Mobile1:
    def __init__(self):
        print("Inside constructor")
    def purchase (self):
        print("Purchasing a mobile")
mob1=Mobile1()
mob1.purchase() #Inbound method invocation, We need not pass the value for self.
Mobile1.purchase(mob1) #Outbound method invocation, We have to pass the object as the value of self.