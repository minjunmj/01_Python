def calculate_price(price, rate=0.1):
    final_price = price*(1-rate)
    discount = price*rate

    return final_price, discount

final_price, discount = calculate_price(100_000)
print(f"할인 금액 : {discount}")
print(f"최종 가격: {final_price}")
final_price, discount = calculate_price(100_000, 0.2)
print(f"할인 금액 : {discount}")
print(f"최종 가격: {final_price}")
final_price, discount = calculate_price(100_000, rate=0.3)
print(f"할인 금액 : {discount}")
print(f"최종 가격: {final_price}")
