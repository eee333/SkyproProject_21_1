import os
from field import Field, Cell
from terrain import Door, Key, Wall, Grass, Trap
from unit import Ghost


class GameController:
    def __init__(self, cell_mapping, level_str):
        self.cell_mapping = cell_mapping
        self.level_str = level_str
        self.unit = None
        self.game_on = True
        self.field = Field(self._make_field(), self.unit)

    def _make_field(self):  # Создаем Двумерный массив объектов класса Cell
        field_array = []
        for y, line in enumerate(self.level_str.split('\n')):
            line_obj = []
            for x, letter in enumerate(line):

                if letter == "W":
                    line_obj.append(Cell(Wall()))
                if letter == "g":
                    line_obj.append(Cell(Grass()))
                if letter == "T":
                    line_obj.append(Cell(Trap()))
                if letter == "K":
                    line_obj.append(Cell(Key()))
                if letter == "D":
                    line_obj.append(Cell(Door()))
                if letter == "G":
                    self.unit = Ghost(100, (x, y))  # Создаем героя, но на поле не добавляем.
                    line_obj.append(Cell(Grass()))
            field_array.append(line_obj)
        return field_array

    def _draw_field(self):
        os.system('cls')  # Очистка экрана перед выводом. Не работает в IDE
        unit_coord = self.unit.get_coordinates()
        print(f"Ghost hp: {self.unit.get_hp()}, key: {self.unit.has_key()}")
        for y, line in enumerare(self.field.get_field()):
            line_str = ""
            for x, item in enumerate(line):
                item_obj = item.get_obj()
                if unit_coord == (x, y):
                    item_class = "Ghost"  # Рисуем героя на поле.
                else:
                    item_class = item_obj.get_terrain()
                line_str += self.cell_mapping[item_class]
            print(line_str)

    def play(self):
        self._draw_field()
        while self.game_on and not self.hero.escaped:
            command = input()
            if command == "w":
                self.field.move_unit_up()
            if command == "s":
                self.field.move_unit_down()
            if command == "a":
                self.field.move_unit_left()
            if command == "d":
                self.field.move_unit_right()
            if command == "z":
                break
            self._draw_field()
         
        if self.unit.has_escaped():
            print("Поздравляю! Вам удалось сбежать!\nНажмите Enter, что бы выйти.")
            input()
