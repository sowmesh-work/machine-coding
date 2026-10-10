from vehicle import Vehicle
from vehicle_size import VehicleSize

class Bike(Vehicle):
    def __init__(self, license_number, size):
        super().__init__(self, license_number, VehicleSize.SMALL)