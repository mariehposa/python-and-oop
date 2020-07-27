class Challenge4:
    def __init__(self, typ, food):
        self.typ = typ
        self.food = food

    def _setter(self, food):
        if food is None:
            raise Exception ("Food cannot be null")

        self._food = food
    
    def _getter(self):
        return "{} is a food".format(self.food)

    food = property(_getter, _setter)

var = Challenge4('cereal', 'beans')
print(var)