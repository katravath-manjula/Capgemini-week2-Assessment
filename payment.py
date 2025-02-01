class Payment:
    def process_payment(self, amount):
        self.amount = amount  
        print("Processing the payment...")

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        self.amount = amount 
        print(f"Credit Card payment of ${self.amount}...")

class PayPalPayment(Payment):
    def process_payment(self, amount):
        self.amount = amount 
        print(f" PayPal payment of ${self.amount}...")

class BitcoinPayment(Payment):
    def process_payment(self, amount):
        self.amount = amount 
        print(f" Bitcoin payment of {self.amount} BTC...")


payments = [
    CreditCardPayment(),
    PayPalPayment(),
    BitcoinPayment()
]


for payment_method in payments:
    payment_method.process_payment(100)  
