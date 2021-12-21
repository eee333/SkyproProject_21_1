class Terrain:
    def __init__(self, terrain=None, walkable=True):
        self.terrain = terrain
        self.walkable = walkable

    def get_terrain(self):
        return self.terrain

    def is_walkable(self):
        return self.walkable

    def step_on(self, obj):
        pass


class Door(Terrain):
    def __init__(self):
        super().__init__(terrain="Door", walkable=False)

    def step_on(self, obj):
        if obj.has_key():
            obj.set_escaped()
            self.walkable = True


class Key(Terrain):
    def __init__(self):
        super().__init__(terrain="Key", walkable=True)

    def step_on(self, obj):
        obj.set_key()
        self.terrain = "Grass"


class Trap(Terrain):
    def __init__(self, damage=10):
        super().__init__(terrain="Trap", walkable=True)
        self.damage = damage

    def step_on(self, obj):
        obj.get_damage(self.damage)


class Grass(Terrain):
    def __init__(self):
        super().__init__(terrain="Grass", walkable=True)


class Wall(Terrain):
    def __init__(self):
        super().__init__(terrain="Wall", walkable=False)

