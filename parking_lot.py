class ParkingLot:
    def __init__ (self, name, isAdmin = False):
        self.name = name
        self.isAdmin = isAdmin

class CarHandler:
    def __init__(self, name):
        super.__init__(name)
        self.cars_in_lot = []

class CarOwnner:
    def __init__(self, name, car_name):
        super.__init__(name)
        self.car_name = car_name