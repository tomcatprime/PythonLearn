class Unit:
    def __init__(self, name, pos_x, pos_y):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x_1, y_1, x_2, y_2):
        if self.pos_x >= x_1 and self.pos_x <= x_2:
            if self.pos_y >= y_1 and self.pos_y <= y_2:
                return True
        else:
            return False


class Dragon(Unit):
    def __init__(self, name, pos_x, pos_y, fire_range):
        super().__init__(name, pos_x, pos_y)
        self.__fire_range = fire_range

    def breathe_fire(self, x, y, units):
        x_1 = x - self.__fire_range
        y_1 = y - self.__fire_range
        x_2 = x + self.__fire_range
        y_2 = y + self.__fire_range

        units_hit = []
        
        for unit in units:
            if unit.in_area(x_1, y_1, x_2, y_2):
                units_hit.append(unit)
        return units_hit