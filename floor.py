from vehicle import Vehicle
from vehicle_size import VehicleSize
from parking_spot import ParkingSpot

class Floor:
    def __init__(self,floor_number):
        self.floor_number = floor_number
        self.spots: list[ParkingSpot] = []

    def add_spot(self, spot: ParkingSpot):
        self.spots.append(spot)

    def find_spot(self, vehicle:Vehicle):
        for spot in self.spots:
            if spot.can_fit(vehicle):
                return spot
        return None

    def get_available_count(self,size:VehicleSize):
        count = 0
        for spot in self.spots:
            if spot.is_available() and spot.get_size() == size:
                count+=1
        return count
