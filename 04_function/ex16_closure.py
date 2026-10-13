def create_account(balance):
    x = balance
    def deposit(amount):
        nonlocal x
        x += amount
        return x

    return deposit

account = create_account(10_000)

print(account(5000))
print(account(3000))
print(account(2000))