class BankAccount:
    def __init__(self, account_holder: str, balance: float = 0.0) -> None:
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than 0.")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than 0.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount

    def check_balance(self) -> float:
        return self.balance

    def display_details(self) -> str:
        return f"Account Holder: {self.account_holder}, Balance: ${self.balance:.2f}"


if __name__ == "__main__":
    account = BankAccount("Harshil", 1000)
    account.deposit(500)
    account.withdraw(200)
    print(account.display_details())
