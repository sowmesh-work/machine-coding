from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self,amount):
        pass

class UPIPayment(PaymentMethod):
    def pay(self,amount):
        print(f"Paid ₹{amount} through UPI")
        return True

class CardPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ₹{amount} through card")
        return True

class CashPayment(PaymentMethod):
    def pay(self,amount):
        print(f"Paid ₹{amount} through cash")
        return True