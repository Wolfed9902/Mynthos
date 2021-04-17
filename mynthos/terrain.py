# Mynthos Terrain Class

class TerrainTile:

    def __init__(self, type):
        self.type = type
        self.passable = True
        self.selected = False
        self.temperature = 70

    def __repr__(self):
        return self.type

    # static_placement
