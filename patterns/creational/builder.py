class House:
    footing = False
    walls = False
    roof = False
    garage = False
    pool = False
    chimney = False

class HouseBuilder:
    house = None

    def __init__(self):
        self.house = House()

    def build_footing(self):
        self.house.footing = True
        return self

    def build_walls(self):
        self.house.walls = True
        return self

    def build_roof(self):
        self.house.roof = True
        return self

    def build_pool(self):
        self.house.pool = True
        return self

    def build_chimney(self):
        self.house.chimney = True
        return self

    def get_result(self):
        return self.house
