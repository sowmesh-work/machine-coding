from datetime import datetime
import uuid
import math

from vehicle import Vehicle
from parking_spot import ParkingSpot

class Ticket:
    def __init__(self, spot: ParkingSpot, vehicle: Vehicle):
        self.ticket_id = str(uuid.uuid4())
        self.spot = spot
        self.vehicle = vehicle
        self.entry_time = datetime.now()
        self.exit_time = None
        
    def close(self):
        self.exit_time = datetime.now()

    def get_duration_hours(self):
        if self.exit_time is None:
            raise ValueError("The vehicle is still parked")
        duration = self.exit_time - self.entry_time
        hours = math.ceil(duration.total_seconds()/3600)
        return hours