class Challenge4:
    def __init__(self, type, food):
        self.type = type
        self.food = food

    def _setter(self, type, food):
        if food is None:
            raise Exception ("Food cannot be null ")
    