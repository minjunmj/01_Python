scores = [70, 85, 95, 100, 60]

# result = lambda score : score+5 if score <= 95 else 100
result = lambda score : min(score+5,100)
print(list(map(result, scores)))


members = [
    {"name": "Kim", "price": 800000},
    {"name": "Lee", "price": 300000},
    {"name": "Park", "price": 1200000},
    {"name": "Choi", "price": 450000},
    {"name": "Jung", "price": 650000}
]