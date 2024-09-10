# Write a Python program to generate tickets for online bus booking, based on the class diagram given below.
import random

class Booking:
    counter = 0
    def __init__(self, passenger_name, source, destination):
        self.__passenger_name = passenger_name
        self.__source = source 
        self.__destination = destination
        self.__ticket_id = None
        self.generate_ticket()

    
    def validate_source_destination(self, source, destination):
        destinations = ["Chennai", "Mumbai", "Kolkata", "Delhi", 'Pune']
        if source == "Delhi" and destination in destinations:
            return True
        else:
            print("Invalid destination")
            return False

    def generate_ticket(self):
        if self.validate_source_destination(self.__source, self.__destination):
            print("Valid")
            Booking.counter += 1
            self.__ticket_id = self.__source[0] + self.__destination[0] + str(Booking.counter) + "-" + str(random.randint(0,100)) + str(random.randint(0, 100))
        else:
            self.__ticket_id = None
        
        
        
    def get_passenger_name(self):
        return f"Passenger {self.__passenger_name}"
    def get_source(self):
        return f"Source {self.__source}"
    
    def get_destination(self):
        return f"Destination {self.__destination}"
    
    def get_ticket_id(self):
        return f"Ticket ID {self.__ticket_id}"
    



passenger1 = Booking("John", "Delhi", "Mumbai")
print(passenger1.get_passenger_name())  # Output: Passenger John
print(passenger1.get_source())  # Output: Source Delhi
print(passenger1.get_destination())  # Output: Destination Mumbai
print(passenger1.get_ticket_id())  # Output: Ticket ID <random ticket ID>

print("###################")
print("###################")
print("###################")
print("###################")

passenger2 = Booking("Jane", "Delhi", "Kolkata")
print(passenger2.get_passenger_name())  # Output: Passenger Jane
print(passenger2.get_source())  # Output: Source Delhi
print(passenger2.get_destination())  # Output: Destination Kolkata
print(passenger2.get_ticket_id())  # Output: Ticket ID <random ticket ID>

print("###################")
print("###################")
print("###################")
print("###################")

passenger3 = Booking("John", "Pune", "Mumbai")
print(passenger3.get_passenger_name())  # Output: Passenger John
print(passenger3.get_source())  # Output: Source Pune
print(passenger3.get_destination())  # Output: Destination Mumbai
print(passenger3.get_ticket_id())  # Output: Invalid destination, Ticket ID None
passenger3.generate_ticket()  # Output: Invalid destination

print("###################")
print("###################")
print("###################")
print("###################")

passenger4 = Booking("Jane", "Delhi", "Chennai")
print(passenger4.get_passenger_name())  # Output: Passenger Jane
print(passenger4.get_source())  # Output: Source Delhi
print(passenger4.get_destination())  # Output: Destination Chennai
print(passenger4.get_ticket_id())  # Output: Ticket ID <random ticket ID>
passenger4.generate_ticket()  # Output: Valid, Ticket ID generated
