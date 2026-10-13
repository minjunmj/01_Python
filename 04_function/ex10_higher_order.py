def normal_discount(price):
    return float(price)
	# 할인 없음

def gold_discount(price):
    return 0.9*price
	# 10% 할인

def vip_discount(price):
    return 0.8*price
	# 20% 할인

def calculate_price(price, discount_func):
    return discount_func(price)
	# 전달받은 함수 실행

print(calculate_price(100_000, normal_discount))
print(calculate_price(100_000, gold_discount))
print(calculate_price(100_000, vip_discount))