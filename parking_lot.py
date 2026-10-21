from floor import Floor
from vehicle import Vehicle
from ticket import Ticket
from pricing_strategy import PricingStrategy
from payment import PaymentMethod


class ParkingLot:
    def __init__(self, pricing: PricingStrategy):
        self.floors: list[Floor] = []
        self.pricing = pricing
        self.active_tickets: dict[str, Ticket] = {}

    def add_floor(self, floor: Floor):
        self.floors.append(floor)

    def park_vehicle(self, vehicle: Vehicle) -> Ticket:
        spot = self._find_spot(vehicle)
        if spot is None:
            raise ValueError("Sorry, no free spot for this vehicle")

        spot.park(vehicle)
        ticket = Ticket(spot, vehicle)
        self.active_tickets[ticket.ticket_id] = ticket
        return ticket

    def exit_vehicle(self, ticket_id: str, payment: PaymentMethod) -> float:
        ticket = self.active_tickets.get(ticket_id)
        if ticket is None:
            raise ValueError("Invalid ticket")

        ticket.close()
        fee = self.pricing.calculate_fee(ticket)

        if not payment.pay(fee):
            raise ValueError("Payment failed")

        ticket.spot.unpark()
        del self.active_tickets[ticket_id]
        return fee

    def _find_spot(self, vehicle: Vehicle):
        for floor in self.floors:
            spot = floor.find_spot(vehicle)
            if spot is not None:
                return spot
        return None