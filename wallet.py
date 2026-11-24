class Wallet():
    def __init__(self, balance=0):
        self.balance = balance

    def add_cash(self, amount):
        self.balance += amount

    def spend_cash(self, amount):
        if amount > self.balance:
            raise InsufficientAmount(
                f"Insufficient amount in wallet. Current balance: "
                f"{self.balance}, requested: {amount}"
            )
        self.balance -= amount


class InsufficientAmount(Exception):
    pass
