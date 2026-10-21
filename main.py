from vehicle_size import VehicleSize
from car import Car
from bike import Bike
from truck import Truck
from parking_spot import ParkingSpot
from floor import Floor
from pricing_strategy import HourlyPricing
from payment import UPIPayment, CashPayment
from parking_lot import ParkingLot

# Build one floor with one spot of each size
floor = Floor(1)
floor.add_spot(ParkingSpot(1, VehicleSize.SMALL))
floor.add_spot(ParkingSpot(2, VehicleSize.MEDIUM))
floor.add_spot(ParkingSpot(3, VehicleSize.LARGE))

# Wire up the lot (prices are decided here, not inside the classes)
pricing = HourlyPricing({
    VehicleSize.SMALL: 20,
    VehicleSize.MEDIUM: 50,
    VehicleSize.LARGE: 100,
})
lot = ParkingLot(pricing)
lot.add_floor(floor)

print("1. A car arrives")
car_ticket = lot.park_vehicle(Car("KA01AB1234"))
print(f"   Parked at spot {car_ticket.spot.get_spot_number()}")
print(f"   Free medium spots left: {floor.get_available_count(VehicleSize.MEDIUM)}")

print("2. A bike arrives")
bike_ticket = lot.park_vehicle(Bike("KA02CD5678"))
print(f"   Parked at spot {bike_ticket.spot.get_spot_number()}")

print("3. A truck arrives")
truck_ticket = lot.park_vehicle(Truck("KA03EF4321"))
print(f"   Parked at spot {truck_ticket.spot.get_spot_number()}")

print("4. A second car arrives")
try:
    lot.park_vehicle(Car("KA05XY9999"))
except ValueError as e:
    print(f"   {e}")

print("5. The first car leaves, paying by UPI")
fee = lot.exit_vehicle(car_ticket.ticket_id, UPIPayment())
print(f"   Total: ₹{fee}")
print(f"   Free medium spots left: {floor.get_available_count(VehicleSize.MEDIUM)}")

print("6. The truck leaves, paying cash")
fee = lot.exit_vehicle(truck_ticket.ticket_id, CashPayment())
print(f"   Total: ₹{fee}")

print("7. Someone tries the car's ticket again")
try:
    lot.exit_vehicle(car_ticket.ticket_id, UPIPayment())
except ValueError as e:
    print(f"   {e}")
