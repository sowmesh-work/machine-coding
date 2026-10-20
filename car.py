from vehicle import Vehicle
from vehicle_size import VehicleSize

class Car(Vehicle):
    def __init__(self, license_number):
        super().__init__(license_number,VehicleSize.MEDIUM)