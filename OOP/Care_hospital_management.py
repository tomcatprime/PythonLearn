class LabtestRepository:
    list_of_hospital_test_ids = [1855, 1856, 1857, 1858, 1859, 2098, 2789, 2345, 1236,]
    # in dollars
    list_of_lab_test_charge = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65]

    def __init__(self):
        pass

    def get_test_charge(self, lab_test_id):
        index = self.list_of_hospital_test_ids.index(lab_test_id)
        return self.list_of_lab_test_charge[index]
        
class Patient:
    def __init__(self, patient_id, patient_name, list_of_lab_tests_ids):
        self.patient_id = patient_id
        self.patient_name = patient_name
        self.list_of_lab_tests_ids = list_of_lab_tests_ids
        

    def calculate_lab_test_charge(self, list_of_lab_tests_ids):
        total_charge = 0
        for lab_test_id in list_of_lab_tests_ids:
            lab_test_charge = LabtestRepository().get_test_charge(lab_test_id)
            total_charge += lab_test_charge
            print(f"Lab test {lab_test_id} charge: ${lab_test_charge}")
        return total_charge 
    

