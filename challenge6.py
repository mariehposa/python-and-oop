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