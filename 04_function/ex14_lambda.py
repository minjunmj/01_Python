members = [
    {"name": "Kim", "price": 800000},
    {"name": "Lee", "price": 300000},
    {"name": "Park", "price": 1200000},
    {"name": "Choi", "price": 450000},
    {"name": "Jung", "price": 650000}
]

print(list(filter(lambda x : x['price']>=500000, members)))

