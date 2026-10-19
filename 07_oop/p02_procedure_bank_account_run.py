def deposit(balance, amount):
    return balance + amount

def withdraw(balance, amount):
    if amount > balance:
        print("잔액이 부족합니다")
        return balance

    return balance - amount

def show_balance(balance):
    print(f"현재 잔액: {balance}")

def main():
    balance = 100_000
    balance = deposit(balance, 50_000)
    balance = withdraw(balance, 30_000)

    show_balance(balance)

if __name__ == "__main__":
    main()