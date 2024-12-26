class Human:
    def sprint_right(self):
        if self.__stamina > 0:
            Human.__use_sprint_stamina(self)
            Human.move_right(self)
            Human.move_right(self)
        else:
            
            Human.__raise_if_cannot_sprint(self)
            
            
    def sprint_left(self):
        if self.__stamina > 0:
            Human.__use_sprint_stamina(self)
            Human.move_left(self)
            Human.move_left(self)
        else:
            Human.__raise_if_cannot_sprint(self)

    def sprint_up(self):
        if self.__stamina > 0:
            Human.__use_sprint_stamina(self)
            Human.move_up(self)
            Human.move_up(self)
        else:
            
            Human.__raise_if_cannot_sprint(self)

    def sprint_down(self):
        if self.__stamina > 0:
            Human.__use_sprint_stamina(self)
            Human.move_down(self)
            Human.move_down(self)
        else:
            
            Human.__raise_if_cannot_sprint(self)

    def __raise_if_cannot_sprint(self):
        raise Exception("not enough stamina to sprint")

    def __use_sprint_stamina(self):
        self.__stamina -= 1
    # don't touch below this line

    def move_right(self):
        self.__pos_x += self.__speed

    def move_left(self):
        self.__pos_x -= self.__speed

    def move_up(self):
        self.__pos_y += self.__speed

    def move_down(self):
        self.__pos_y -= self.__speed

    def get_position(self):
        return self.__pos_x, self.__pos_y

    def __init__(self, pos_x, pos_y, speed, stamina):
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        self.__speed = speed
        self.__stamina = stamina
