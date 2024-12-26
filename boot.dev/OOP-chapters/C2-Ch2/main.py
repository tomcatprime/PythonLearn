class Student:
    def __init__(self, name):
        self.name = name
        self.__courses = {}
        
    def calculate_letter_grade(self, score):
        if score >= 90:
            return "A"
        elif score >= 80 and score <= 89:
            return "B"
        elif score >= 70 and score <= 79:
            return "C"
        elif score >= 60 and score <= 69:
            return "D"
        else:
            return "F"

    def add_course(self, course_name, score):
        score_value = Student.calculate_letter_grade(self, score)
        self.__courses[course_name] = score_value
        
    def get_courses(self):
        return self.__courses
