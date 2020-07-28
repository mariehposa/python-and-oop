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
test3 = Challenge5('jeff')
print(Challenge5.get_count())



class withoutClassMethod():
    count = 0

    def __init__(self):
        withoutClassMethod.count += 1

    def get_counts():
        return (f"withoutClassMethod has {withoutClassMethod.count} class instances")

test1 = withoutClassMethod()
test2 = withoutClassMethod()
test3 = withoutClassMethod()
print(withoutClassMethod.get_counts())