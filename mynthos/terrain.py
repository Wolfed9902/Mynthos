# Mynthos Terrain Class

class TerrainTile:

    def __init__(self, type):
        self.type = type
        self.passable = True
        self.selected = False

    def __repr__(self):
        return self.type


    # modifiable

    # static_placement
