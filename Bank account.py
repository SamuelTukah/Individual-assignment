# bankaccount
"""Question 1a - BankAccount class with private balance and test usage."""

class BankAccount:
    def __init__(self, initial_balance=0.0):
        self._balance = float(initial_balance)

    def deposit(self, amount):
        """Add money to the account. Returns new balance."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount
        return self._balance

    def withdraw(self, amount):
        """Withdraw money if sufficient funds exist. Returns new balance."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self._balance:
            print(f"Withdrawal failed: insufficient funds (balance={self._balance}, requested={amount})")
            return self._balance
        self._balance -= amount
        return self._balance

    def get_balance(self):
        """Return the current balance."""
        return self._balance

if __name__ == "__main__":
    acc1 = BankAccount(50)
    acc2 = BankAccount(10)

    print("Initial balances:", acc1.get_balance(), acc2.get_balance())

    acc1.deposit(100)
    print("acc1 after deposit 100:", acc1.get_balance())

    acc1.withdraw(30)
    print("acc1 after withdraw 30:", acc1.get_balance())

    acc2.withdraw(15)  
    print("acc2 after failed withdraw 15:", acc2.get_balance())

    acc2.deposit(50)
    acc2.withdraw(20)
    print("acc2 final balance:", acc2.get_balance())
