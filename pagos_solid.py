from abc import ABC, abstractmethod

# 1. Interfaz (Contrato)
class PaymentMethod(ABC):

    @abstractmethod
    def pay(self, amount: float):
        pass


# 2. Implementaciones concretas

class PayPalPayment(PaymentMethod):

    def pay(self, amount: float):
        print(f"Pagando ${amount} usando PayPal")


class StripePayment(PaymentMethod):

    def pay(self, amount: float):
        print(f"Pagando ${amount} usando Stripe")


# 3. Clase de alto nivel

class PaymentProcessor:

    def __init__(self, payment_method: PaymentMethod):
        self.payment_method = payment_method

    def process_payment(self, amount: float):
        print("Procesando pago...")
        self.payment_method.pay(amount)
        print("Pago completado")


# --- Uso del sistema ---

if __name__ == "__main__":

    # Pago con PayPal
    paypal = PaymentProcessor(PayPalPayment())
    paypal.process_payment(100)

    print()

    # Pago con Stripe
    stripe = PaymentProcessor(StripePayment())
    stripe.process_payment(200)