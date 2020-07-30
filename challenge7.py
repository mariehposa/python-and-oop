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

    def details(self):
        print(f'Food contains {self.carbohydrates.name} as carbohydrate, {self.proteins.name} as protein and {self.fats.name} as fat')

food = Foods(Carbohydrates('rice'), Proteins('beans'), Fats('cheese'))
food.details()