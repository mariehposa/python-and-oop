class ParkingLot:
    def __init__ (self, name, car_name, isAdmin = False):
        self.name = name
        self.car_name = car_name
        self.isAdmin = isAdmin

class Handler:
    def __init__(self, name):
        super.__init__(name)
        self.cars_in_lot = []
