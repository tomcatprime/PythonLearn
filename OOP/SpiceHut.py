from abc import ABC, abstractmethod

class Customer(ABC):
    # Abstract base class (ABC) with common attributes and methods for customers

    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.bill_amount = 0
        self.bill_id = None


    @abstractmethod
    def calculate_bill_amount(self):
        # Abstract method, must be implemented by subclasses
        pass

    def get_customer_name(self):
        # Getter for customer_name
        return self.customer_name

class OccasionalCustomer(Customer):
    """
    Attributes:
        distance_in_kms (int): The delivery distance in kilometers.
        counter (int): A static counter for generating bill IDs (starts at 1000).
    """
    counter = 1000
    price_per_km = None
    def __init__(self, customer_name, distance_in_kms):
        """
        Initializes a new OccasionalCustomer object.
        Args:
        customer_name (str): The name of the customer.
        distance_in_kms (int): The delivery distance in kilometers.
        """
        super().__init__(customer_name)
        self.distance_in_kms = distance_in_kms
        OccasionalCustomer.counter += 1
        self.bill_id = '0' + str(OccasionalCustomer.counter)
    def validate_distance_in_kms(self):
    # bool: True if the distance is between 1 and 5 (inclusive), False otherwise.
        return 1 <= self.distance_in_kms <= 5

    def calculate_bill_amount(self):


s1 = Customer("Karol")
print(s1.get_customer_name())
print(s1.counter)
s2 = Customer("Szejker")
print(s1.bill_id)
print(s2.bill_id)