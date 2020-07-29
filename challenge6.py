class Engineering:
    def __init__(self, name, rank, company):
        self.name = name
        self.rank = rank
        self.company = company

    def get_info(self):
        print(f'{self.name} is a {self.rank} at {self.company}')

class Software(Engineering):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary =  salary

    def get_info(self):
        print(f'{self.name} salary as a software engineer is {self.salary}')

class Hardware(Engineering):
    def __init__(self, name):
        super().__init__(name)

    def get_info(self):
        print(f'{self.name} is a hardware engineer')

parent = Engineering('cassidy williams', 'senior developer', 'netlify')
first_child = Software('angie jones', '$150000')