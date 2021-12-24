class Field:
    def __init__(self, field_array, unit):
        self.field_array = field_array  # Двумерный массив объектов класса Cell
        self.unit = unit

    def cell(self, coord):  # метод, возвращающий объект находящийся по данным координатам;
        x, y = coord
        return self.field_array[y][x]
    
    def _do_move(self, x, y):
       step_on_obj = self.cell((x, y)).get_obj()
        step_on_obj.step_on(self.unit)
        if step_on_obj.is_walkable():
            self.unit.set_coordinates((x, y))
    
    def move_unit_up(self):  # метод, смещающий юнита вверх;
        x, y = self.unit.get_coordinates()
        self._do_move(x, y-1)

    def move_unit_down(self):  # метод, смещающий юнита вниз;
        x, y = self.unit.get_coordinates()
        self._do_move(x, y+1)

    def move_unit_right(self):  # метод, смещающий юнита вправо;
        x, y = self.unit.get_coordinates()
        self._do_move(x+1, y)

    def move_unit_left(self):  # метод, смещающий юнита влево;
        x, y = self.unit.get_coordinates()
        self._do_move(x-1, y)

    def get_field(self):  # возвращает свойство field.
        return self.field_array


class Cell:
    def __init__(self, obj=None):
        self.obj = obj

    def get_obj(self):
        return self.obj

    def set_obj(self, obj):
        self.obj = obj
