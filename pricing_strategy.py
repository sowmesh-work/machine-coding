from abc import ABC,abstractmethod

from ticket import Ticket

class PricingStrategy(ABC):
    @abstractmethod
    def calculate_fee(self,ticket:Ticket):
        pass

class HourlyPricing(PricingStrategy):
    
    def __init__(self,rates):
        self.rates = rates
    def calculate_fee(self,ticket:Ticket):
        hour = ticket.get_duration_hours()
        size = ticket.vehicle.get_size()
        return hour*self.rates[size]