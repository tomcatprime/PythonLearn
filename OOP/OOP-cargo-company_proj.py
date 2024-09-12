import random
class Customer:
    def __init__(self, customer_id, customer_name, address):
        self.__customer_id = customer_id
        self.__customer_name = customer_name
        self.__address = address
        
    def validate_customer_id(self):
        
        if len(self.__customer_id) == 6 and self.__customer_id[0] == "1":
            print(self.__customer_id)
            return True
        else:
            print(self.__customer_id)
            print(self.__customer_id[0])
            return False
        
        
    def get_customer_id(self):
        print(self.__customer_id)
        
    def get_customer_name(self):
        print(self.__customer_name)
        
        
        
class Freight:
    counter = 198
    def __init__(self, recipient_customer, from_customer, weight, distance):
        self.__freight_id = None
        self.__recipient_customer = recipient_customer
        self.__from_customer = from_customer
        self.__weight = weight
        self.__distance = distance
        self.freight_charge = 0
    
    def validate_weight(self):
        if self.__weight % 5 == 0:
            return True
        else:
            return False
        
    def validate_distance(self):
        if self.__distance > 500 and self.__distance < 5000:
            return True
        else:
            return False
        
    def get_freight_charge(self):
        freight_weight_charge = 150
        freight_distance_charge = 60
        total_charge = self.__weight * freight_weight_charge + self.__distance * self.__distance
        return total_charge
    
    def get_recipiet_customer(self):
        return self.__recipient_customer
    
    def get_from_customer(self):
        return self.__from_customer
    
    def get_weight(self):
        return self.__weight
    
    def get_distance(self):
        return self.__distance
    
    def get_freight_id(self):
        return self.__freight_id
    
    def forward_cargo(self):
        if ( self.__from_customer.validate_customer_id() and 
             self.__recipient_customer.validate_customer_id() and
             self.validate_distance() and
             self.validate_weight()
        ):
            Freight.counter += 2
            self.__freight_id = Freight.counter

            print(Freight.get_freight_charge(self))
            print("printing from forward cargo")
            return True
        
        else:
            self.__freight_id = 0
            return False



            
from_customer = Customer("123456", "John Doe", "123 Street A")
recipient_customer = Customer("134567", "Jane Smith", "456 Street B")

# Create Freight object
freight = Freight(recipient_customer, from_customer, weight=50, distance=1000)

if freight.forward_cargo():
    print(f"Freight ID: {freight.get_freight_id()}")
    print(f"Freight Charge: {freight.get_freight_charge()}")
else:
    print("Validation failed. Freight charge set to 0.")
