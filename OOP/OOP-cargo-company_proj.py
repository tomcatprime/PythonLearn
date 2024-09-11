class Customer:
    def __init__(self, customer_id, customer_name, address):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.address = address
        
    def validate_customer_id(self):
        if len(self.customer_id) == 6 and self.customer_id[0] == 1:
            print(self.customer_id)
            return True
        else:
            print(self.customer_id)
            print(self.customer_id[0])
            return False
        
        
    def get_customer_id(self):
        print(self.customer_id)
        
    def get_customer_name(self):
        print(self.customer_name)
        
        
        
class Freight:
    counter = 198
    def __init__(self, recipient_customer, from_customer, weight, distance):
        self.recipient_customer = recipient_customer
        self.from_customer = from_customer
        self.weight = weight
        self.distance = distance
    
    def validate_weight(self):
        if self.weight % 5 == 0:
            return True
        else:
            return False
        
    def validate_distance(self):
        if self.distance > 500 and self.distance < 5000:
            return True
        else:
            return False
        
    def get_freight_charge(self):
        freight_weight_charge = 150
        freight_distance_charge = 60
        total_charge = self.weight * freight_weight_charge + self.distance * self.distance
        return total_charge
    
    def get_recipiet_customer(self):
        return self.recipient_customer
    
    def get_from_customer(self):
        return self.from_customer
    
    def get_weight(self):
        return self.weight
    
    def get_distance(self):
        return self.distance
    
        
customer1 = Customer("123456", "John Doe", "123 Main St")

customer2 = Customer("654321", "Jane Smith", "456 Oak Ave")
Freight1 = Freight("doe", "con2", 25, 600)
print(Freight1.get_freight_charge())
print(Freight1.get_recipiet_customer())
print(Freight1.get_from_customer())
print(Freight1.get_weight())
print(Freight1.get_distance())
print(Freight1.validate_distance())
print("######################")
print(customer1.validate_customer_id()) 

