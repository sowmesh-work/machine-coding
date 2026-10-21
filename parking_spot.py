from vehicle import Vehicle
from vehicle_size import VehicleSize

class ParkingSpot:
    def __init__(self,spot_number:int,size:VehicleSize):
        self.spot_number = spot_number
        self.size = size
        self.vehicle = None

    def is_available(self):
        return self.vehicle is None
    
    def get_spot_number(self):
        return self.spot_number
    
    def get_size(self):
        return self.size
    
    def can_fit(self,vehicle:Vehicle):
        if not self.is_available():
            return False
        return self.size == vehicle.get_size()

    def park(self,vehicle:Vehicle):
        if not self.can_fit(vehicle):
            raise ValueError(f"spot {self.spot_number} cant fit this vehicle")
        self.vehicle = vehicle

    def unpark(self):
        if self.is_available():
            raise ValueError(f"Spot {self.spot_number} is already empty")
        vehicle = self.vehicle
        self.vehicle = None
        return vehicle