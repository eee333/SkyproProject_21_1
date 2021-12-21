class Unit:
    def __init__(self, hp=100, coord=(0, 0)):
        self.hp = hp
        self.got_key = False
        self.coord = coord
        self.escaped = False

    def has_key(self):  # bool — проверяет, есть ли у данного юнита ключ.
        return self.got_key

    def set_key(self):  # — ставит маркер got_key в True.
        self.got_key = True

    def has_escaped(self):  # → bool — проверяет, удалось ли сбежать.
        return self.escaped

    def set_escaped(self):  # → bool — проверяет, удалось ли сбежать.
        self.escaped = True

    def is_alive(self):  # → bool — проверяет, есть ли еще у юнита положительное количество хит-поинтов.
        if self.hp <= 0:
            raise UnitDied('Трагически погиб в неравном бою')
        return True

    def get_hp(self):  # → tuple — возвращает координаты юнита.
        return self.hp

    def get_damage(self, damage):  # — обрабатывает входящий урон с учетом текущего параметра защиты.
        self.hp -= damage  # Если юнит умирает после атаки, должно быть выброшено исключение UnitDied.
        self.is_alive()

    def set_coordinates(self, coord):  # — устанавливает координаты юнита.
        self.coord = coord

    def get_coordinates(self):  # → tuple — возвращает координаты юнита.
        return self.coord

    def has_position(self, coord):  # bool - проверяет в этих ли координатах установлен юнит
        return self.coord == coord


class UnitDied(Exception):
    pass


class Ghost(Unit):
    def __init__(self, hp=100, coord=(0, 0)):
        super().__init__(hp, coord)
        self.name = "Ghost"
