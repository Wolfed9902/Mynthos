# Mynthos Terrain Class

class terrain_tile:

    color = (255, 255, 255)

    def __init__(self, type):
        #self.type = type
        type_color(type)

    def type_color(type):
        if type == "ocean":
            self.color = (52, 152, 255)
        elif type == "barren":
            self.color = (210, 162, 120)
