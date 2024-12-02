class InvalidMechnicIdException(Exception):
    pass


class Mechanic:
    def __init__(self, machanic_id, specialization, vehicle_count):
        self.machanic_id = machanic_id
        self.specialization = specialization
        self.vehicle_count = vehicle_count
        

    def get_mechanic_id(self):
        return self.machanic_id

    def get_specialization(self):
        return self.specialization
    
    def get_vehicle_count(self):
        return self.vehicle_count
    
    def set_mechanic_id(self, mechanic_id):
        self.mechanic_id = mechanic_id
        
    def set_specialization(self, specialization):
        self.specialization = specialization
        
    def set_vehicle_count(self, vehicle_count):
        self.vehicle_count = vehicle_count


class VehicleService:
    def __init__(self, mechanic_list):
        self.mechanic_list = mechanic_list
    def assign_mechanic_for_service(self, mechanic_id, vehicle_type):
        for mechanic in self.mechanic_list:
            if mechanic.get_mechanic_id() == mechanic_id:
                mechanic.set_vehicle_count(mechanic.get_vehicle_count() + 1)
                return mechanic
        raise InvalidMechnicIdException("Invalid Mechanic Id")
        