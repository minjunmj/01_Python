class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("잔액이 부족합니다")

        self.balance -= amount

    def show_balance(self):
        print(f"예금주: {self.owner}")
        print(f"현재 잔액: {self.balance:,}")

def main():
    account = BankAccount("이상무", 100_000)

    account.deposit(50_000)
    account.withdraw(30_000)
    account.show_balance()


if __name__ == "__main__":
    main()