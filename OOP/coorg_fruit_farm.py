class FruitInfo:
    fruit_name_list = ["Apple", "Guava", "Orange", "Grape", "Sweet Lime"]
    
    fruit_price_list = [200, 80, 70, 110, 60]

    @staticmethod
    def get_fruit_price(fruit_name):
        if fruit_name in FruitInfo.fruit_name_list:
            index = FruitInfo.fruit_name_list.index(fruit_name)
            return FruitInfo.fruit_price_list[index]
        else:
            return -1

    @staticmethod
    def get_fruit_name_list():

        return FruitInfo.fruit_name_list
    
    @staticmethod
    def get_fruit_price_list():
        return FruitInfo.fruit_price_list
    

class Purchase:
    counter = 101

    def __init__(self, customer, fruit_name, quantity):
        self.customer = customer
        self.fruit_name = fruit_name
        self.quantity = quantity
        self.total_price = 0
        self.purchase_id = None
    def calculate_price(self):

        
        
        fruit_price = FruitInfo.get_fruit_price(self.fruit_name)
        self.total_price = fruit_price * self.quantity

        # max and min value in the list
        max_value = max(FruitInfo.get_fruit_price_list())
        min_value = min(FruitInfo.get_fruit_price_list())

        if fruit_price == -1:
            return -1 
        # if price of the frui is maximum among the fruits in the list, apply 2% discount ,
        # if price os the fruit is minimu among the fruits in the list, discount 5%
        # if customer type == "wholesale", additional discount 10%
        if fruit_price == max_value and self.quantity > 1:
            self.total_price *= 0.98 # 2$ discount for maximum price

        if fruit_price == min_value and self.quantity > 5:
            self.total_price *= 0.95 # 5$ discount for minimum price

        if self.customer.get_cust_type() == "wholesale":
            self.total_price *= 0.90 # 10% discount for wholesale customer

        self.purchase_id = f"P{Purchase.counter}"
        Purchase.counter += 1
        
        return self.total_price
    

    def get_purchase_id(self):
        return self.purchase_id

    def get_customer(self, customer):
        return customer.get_customer_name()
    
    def get_quantity(self):
        return self.quantity

    
       

class Customer:
    def __init__(self, customer_name, cust_type):
        self.customer_name = customer_name
        self.cust_type = cust_type
    
    def get_customer_name(self):
        return self.customer_name

    def get_cust_type(self):
        return self.cust_type

# ######################################################
import unittest

class TestFruitInfo(unittest.TestCase):
    
    def test_get_fruit_price(self):
        # Test valid fruit names
        self.assertEqual(FruitInfo.get_fruit_price("Apple"), 200)
        self.assertEqual(FruitInfo.get_fruit_price("Guava"), 80)
        self.assertEqual(FruitInfo.get_fruit_price("Orange"), 70)
        self.assertEqual(FruitInfo.get_fruit_price("Grape"), 110)
        self.assertEqual(FruitInfo.get_fruit_price("Sweet Lime"), 60)
        
        # Test invalid fruit name
        self.assertEqual(FruitInfo.get_fruit_price("Banana"), -1)

    def test_get_fruit_name_list(self):
        expected_fruit_list = ["Apple", "Guava", "Orange", "Grape", "Sweet Lime"]
        self.assertEqual(FruitInfo.get_fruit_name_list(), expected_fruit_list)

    def test_get_fruit_price_list(self):
        expected_price_list = [200, 80, 70, 110, 60]
        self.assertEqual(FruitInfo.get_fruit_price_list(), expected_price_list)


class TestCustomer(unittest.TestCase):
    
    def test_get_customer_name(self):
        customer = Customer("Maddy", "wholesale")
        self.assertEqual(customer.get_customer_name(), "Maddy")

    def test_get_cust_type(self):
        customer = Customer("John", "retail")
        self.assertEqual(customer.get_cust_type(), "retail")
