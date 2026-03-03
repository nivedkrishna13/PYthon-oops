class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    @staticmethod
    def validate_amount(amount):
        return amount > 0

    def deposit(self, amount):
        if BankAccount.validate_amount(amount):
            self.balance += amount

    