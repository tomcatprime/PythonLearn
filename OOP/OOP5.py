
class Student:
    def __init__(self, course_id, age, mark, name):
        self.course_id = course_id
        self.age = age
        self.mark = mark
        self.name = name
        self.choose_course()
        self.check_qualification()
    def validate_marks(self):
        if self.mark >= 0 and self.mark <= 100:
            return True
        else:
            return False
    def validate_age(self):
        if self.age > 20:
            return True
        else:
            print("Age should be greater than 20")
            return False
        
    def choose_course(self):
        if self.course_id == 1001:
            if self.mark > 85:
                discount = 0.25
                self.fee = float(25575.0 - (25575.0 * discount))
                print("Discount applied")
            else:
                self.fee = float(25575.0) 
                print("No discount")
            print(f"Course chosen by {self.name} is Biology")
            print(f"Fee for the course is {self.fee}")
            return True
        
        elif self.course_id == 1002:
            if self.mark > 85:
                discount = 0.25
                self.fee = float(25575.0 - (25575.0 * discount))
                print("Discount applied")
            else:
                self.fee = float(25575.0) 
                print("No discount")
            print(f"Course chosen by {self.name} is Biology")
            print(f"Fee for the course is {self.fee}")
            
            return True
        
        else:
            print("Invalid course ID")
            return False

    
    def check_qualification(self ):
        if self.validate_age() and self.validate_marks():
            if self.mark >= 65:
                print(f"Student {self.name}  has qualified")
                return True
            else:
                print(f"Student {self.name} has not qualified")
                return False
    
student1 = Student(1001, 21, 86, "John")
print("##########")
student2 = Student(1002, 21, 75, "Jane")
print("##########")
student3 = Student(1001, 18, 65, "Bob")
print("##########")
student4 = Student(1002, 23, 55, "Alice")
print("##########")
student5 = Student(1001, 22, 99, "Tom")
print("##########")

