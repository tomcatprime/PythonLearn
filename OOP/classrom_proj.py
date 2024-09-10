class Classroom:
    classroom_list = ["Biology", "Chemistry", "Physics", "Mathematics", "English", "History", "Geography", "Art", "Music", "Drama"]
    def __init__(self, class_room):
        self.name = class_room
        Classroom.search_classroom(class_room)

    @classmethod
    def search_classroom(cls, class_check):
        cls.class_check = class_check
        if class_check in cls.classroom_list:
            print(f"{class_check} is available in left wing.")
        else:
            print(f"{class_check} is not available in left wing.")

topic1 = Classroom("Mathematics")

topic2 = Classroom.search_classroom("English")

topic3 = Classroom("Computer Science")

topic4 = Classroom("Art")