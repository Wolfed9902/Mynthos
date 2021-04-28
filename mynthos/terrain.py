# Mynthos Terrain Class

# Description:
# TerrainTile represents a 'pixel' of terrain on a map, of which size can be designated in settings. Terrain type is equivalent to a 'biome'.

class TerrainTile:

    def __init__(self, type):
        self.type = type
        self.passable = True
        self.selected = False
        self.temperature = 70

    def __repr__(self):
        return self.type

    # static_placement
