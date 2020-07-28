class Challenge5:
    count = 0

    def __init__(self, name):
        Challenge5.count += 1
        self.name = name

    def get_name(self):
        return ('my name is {}'.format(self.name))

    @classmethod
    def get_count(cls):
        return (f"Challenge5 has {cls.count} class instances")