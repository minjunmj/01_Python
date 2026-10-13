products = [
    {"name": "노트북", "price": 1500000},
    {"name": "마우스", "price": 30000},
    {"name": "키보드", "price": 120000},
    {"name": "모니터", "price": 350000}
]

result = sorted(products, key = lambda x : x['price'], reverse=True)
print(result)