class Customer:
    def __init__(self, name, age, phone_no, address):
        self.name = name
        self.age = age
        self.phone_no = phone_no
        self.address = address
    def view_details(self):
        print (self.name, self.age, self.phone_no)
        print (self.address.door_no, self.address.street, self.address.pincode)
    def update_details(self, add):
        self.address = add
        
    def view_address(self, customer):
        self.customer = customer
        print (self.address.door_no, self.address.street, self.address.pincode)
class Address:
    def __init__(self, door_no, street, pincode):
        self.door_no = door_no
        self.street = street
        self.pincode = pincode
    def update_address(self):
        pass
add1=Address(123, "5th Lane", 56001)
add2=Address(567, "6th Lane", 82006)
add3=Address(890, "7th Lane", 56007)
cus1=Customer("Jack", 24, 1234, add1)
cus2=Customer("Jill", 27, 5678, add2)

cus1.view_details()
cus1.update_details(add2)
cus1.view_details()
print(cus1.name)
cus1.update_details(add3)
cus1.view_address(cus1)
cus2.view_address(cus2)


print("$$$$$$$$$$$$$$$$")
print("$$$$$$$$$$$$$$$$")
print("$$$$$$$$$$$$$$$$")
print("$$$$$$$$$$$$$$$$")
print("$$$$$$$$$$$$$$$$")
print("$$$$$$$$$$$$$$$$")
# getter/setter method, private variables
class Customer:
    def __init__(self, name, age, phone_no, address):
        self.name = name
        self.age = age
        self.phone_no = phone_no
        self.address = address
    def view_details(self):
        print (self.name, self.age, self.phone_no)
        print (self.address.get_door_no(), self.address.get_street(), self.address.get_pincode())
class Address:
    def __init__(self, door_no, street, pincode):
        self.__door_no = door_no
        self.__street = street
        self.__pincode = pincode
    def get_door_no(self):
        return self.__door_no
    def get_street(self):
        return self.__street
    def get_pincode(self):
        return self.__pincode
    def set_door_no(self, value):
        self.__door_no = value
    def set_street(self, value):
        self.__street = value
    def set_pincode(self, value):
        self.__pincode = value
    def update_address(self):
        pass
add1=Address(123, "5th Lane", 56001)
cus1=Customer("Jack", 24, 1234, add1)
cus1.view_details()


# Sometimes a class may depend on another class for some of its use. 
# This is not a strict relationship and hence won’t appear in the class diagram.
# For example, in the below code, the Customer class depends on a payment object for purchasing. 
# Here payment is a local variable and not an attribute.

class Customer:
    def __init__(self, name, age, phone_no):
        self.name = name
        self.age = age
        self.phone_no = phone_no
    def purchase(self, payment):
        if payment.type == "card":
            print ("Paying by card")
        elif payment.type == "e-wallet":
            print ("Paying by wallet")
        else:
            print ("Paying by cash")
            
class Payment:
    def __init__(self, type):
        self.type = type
payment1=Payment("card")
c=Customer("Jack",23,1234)
c.purchase(payment1)


# Apart from an object being passed as a parameter to the method, an object can also be created locally inside a method. 
# This is also a weaker dependency which does not reflect in the class diagram.

#Object creation
class Customer:
    def __init__(self, name,cust_type,bill):
        self.name = name
        self.bill = bill
        self.cust_type=cust_type
    def calulate_bill(self):
        tax1=Tax(self.cust_type)
        final_bill=self.bill*tax1.tax_details(self.cust_type)
        return final_bill
class Tax:
    def __init__(self,cust_type):
        self.cust_type=cust_type
    def tax_details(self,cust_type):
        if(cust_type=="Student"):
            return 5
        else:
            return 10
cust1=Customer("Maddy","Student",100)
print(cust1.calulate_bill())