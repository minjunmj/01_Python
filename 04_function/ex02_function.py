name = "Kim"
price = 750_000

def get_grade(price):
    if price >= 1_000_000:
         return "VIP"
    elif price >= 500_000:
         return "GOLD"
    elif price >= 100_000:
         return "SILVER"
    else:
        return "NORMAL"

grade = get_grade(price)

print(name, "회원등급:", grade)