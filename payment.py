from abc import ABC, abstractmethod
from pricing_strategy import PricingStrategy

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self,amount):
        pass

class UPIPayment(PaymentMethod):
    def pay(self,amount):
        print(f"paid{amount} through UPI")
        return True

class CardPayment(PaymentMethod):
    def pay(self, amount):
        print(f"paid{amount} through card")
        return True

class CashPayment(PaymentMethod):
    def pay(self,amount):
        print(f"paid{amount} through cash")
        return True