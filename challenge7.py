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
        print('Food contains {} as carbohydrate, {} as protein and {} as fat'.format(self.carbohydrates.name, self.proteins.name, self.fats.name))

food = Foods(Carbohydrates('rice'), Proteins('beans'), Fats('cheese'))
food.details()