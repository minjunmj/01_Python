def create_discount(rate):

    def discount(price):
        return price*(1.0-rate)

    return discount

normal=create_discount(0)
gold=create_discount(0.1)
vip=create_discount(0.2)

print(normal(100_000))
print(gold(100_000))
print(vip(100_000))