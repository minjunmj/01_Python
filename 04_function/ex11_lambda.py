discount  = lambda price, rate : price*(1-rate)

print(discount(100000, 0.1))
print(discount(200000, 0.2))

check_pass = lambda score : "합격" if score >= 60 else "불합격"

print(check_pass(85))
print(check_pass(45))
print(check_pass(60))