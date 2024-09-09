# # WeCare insurance company wants to calculate premium for vehicles.
# # Vehicles are of two types – "Two Wheelers" and "Four Wheelers". Each vehicle is identified by vehicle id, type, cost, and premium amount.

# # Premium amount is 2% of the vehicle cost for a two wheeler and 6% for four wheeler. Calculate the premium amount and display the vehicle details.

# # Write a Python program to implement the class chosen with its attributes and methods.

# # Display appropriate error message, if the vehicle type is invalid
# # Perform case sensitive string comparison

# Implement the Customer class based on the identified class structure and details given below:

#     1. Consider all instance variables and methods to be public
#     2. Assume that bill_amount is initialized with total bill amount of the customer
#     3. Customer is eligible for 5% discount on the bill amount
#     4. purchases(): Compute discounted bill amount and pay bill
#     5. pays_bill(amount): Display, <customer_name> pays bill amount of Rs. <amount>

# Represent few customers, invoke purchases() method and display the details.

class Main:
    def __init__(self, bill_amount, customer_name, item_id):
        self.customer_name = customer_name
        self.item_id = item_id
        self.bill_amount = bill_amount
        print("Welcome ", self.customer_name, "You have to pay ", self.bill_amount, "for a " + self.item_id)

    def purchase(self, item_id, bill_amount):
        if self.item_id == "Two Wheeler":
            self.bill_amount = self.bill_amount - (self.bill_amount * 0.02)
        elif self.item_id == "Four Wheeler":
            self.bill_amount = self.bill_amount - (self.bill_amount * 0.06)
        else:
            print("Invalid Vehicle Type")
        
mob1 = Main(100000, "Tom", "Two Wheeler")
