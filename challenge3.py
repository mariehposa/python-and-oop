class Challenge3:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'a = {}, y = {}'. format(self.a, self.b)

    def __repr__(self):
        pass

var = Challenge3(1, 2)

print(var)