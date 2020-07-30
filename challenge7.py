class Carbohydrates:
    def __init__(self, name):
        self.name = name

class Proteins:
    def __init__(self, name):
        self.name = name

class Fats:
    def __init__(self, name):
        self.name = name

class Foods:
    def __init__(self, carbohydrates, proteins, fats):
        self.carbohydrates = carbohydrates
        self.proteins = proteins
        self.fats = fats