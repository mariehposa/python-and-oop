class Challenge5():
    count = 0

    def __init__(self, name):
        self.name = name
        Challenge5.count += 1

    def get_name(self):
        return ('my name is {}'.format(self.name))

    @classmethod
    def get_count(cls):
        return (f"Challenge5 has {cls.count} class instances")

test = Challenge5('mariam')
print(test.get_name())

test2 = Challenge5('mark')
test2 = Challenge5('jeff')
print(test.get_count())