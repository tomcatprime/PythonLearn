import random

class Apparel:
    counter = 100
    item_id = None
    price = None

    def __init__(self, price, item_type):
        self.price = price
        self.item_type = item_type.lower()
        Apparel.counter += 1
        if self.item_type == "cotton":
            self.item_id = f"C{Apparel.counter}"
        elif self.item_type == "silk":
            self.item_id = f"S{Apparel.counter}"
        else:
            raise ValueError("Invalid item type. Only 'cotton' or 'silk' is allowed.")


    def calculate_price(self):
        # # Add 5% service tax to the price
        self.price += self.price * 0.05

    def get_item_id(self):
        return self.item_id

    def get_price(self):
        return self.price

    def get_item_type(self):
        return self.item_type

    # setter method for price
    def set_price(self,price):
        self.price = price

class Cotton(Apparel):
    def __init__(self, price, discount):
        #Invoke parent class constructor with "Cotton" as item_type
        super().__init__(price, "Cotton")
        #Initialize the discount attribute
        self.discount = discount
    def calculate_price(self):
        # Apply the discount to the price
        self.price -= self.price * (self.discount / 100)
        # Call the parent class's calculate_price to add the service tax
        super().calculate_price()

    def get_discount(self):
        return self.discount

class Silk(Apparel):
    points = None
    def __init__(self, price):
        #Invoke parent class constructor with "Cotton" as item_type
        super().__init__(price, "Silk")
        super().calculate_price()
        self.price += self.price * 0.10
        if self.price > 10000:
            self.points = 10
        else:
            self.points = 3
    def get_points(self):
        return self.points
s1 = Apparel(2000, "Cotton")
s2 = Apparel(4000, "Silk")

s1.get_item_id()
s2.get_item_id()


# Example Usage
cotton_item = Cotton(1500, 10)  # Price: 1500, Discount: 10%
print(f"Item ID: {cotton_item.get_item_id()}, Price: {cotton_item.get_price()}, Discount: {cotton_item.get_discount()}%")
# Output: Item ID: C101, Price: 1500, Discount: 10%

cotton_item.calculate_price()
print(f"Final Price after Discount and Tax: {cotton_item.get_price()}")
# Output: Final Price after Discount and Tax: 1417.5 (10% discount applied, then 5% tax added)

silk_item = Silk(5000)
silk_item.calculate_price()
print(f"Silk item {silk_item.get_price()}")
print(silk_item.price)
print(silk_item.points)
print(f"From get_points {silk_item.get_points()}")