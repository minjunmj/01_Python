# scores = [80,70,83,82,81]

# print(f'scores[0]: {scores[0]}')
# print(f'scores[2]: {scores[2]}')

# fruits = ['apple', 'orange']

# fruits.insert(1,'banana')
# print(f'fruits: {fruits}')

# a = [10,20]
# b = [30,40]

# a.extend(b)

# print(a)

# fruits = ['apple', 'banana', 'orange']
# fruits.remove("banana")
# print(fruits)

fruits = ['apple', 'banana', 'orange', 'banana']
item = fruits.pop(2)
print(f"item: {item}")
print(f"fruits: {fruits}")

fruits = ['apple', 'banana', 'orange', 'banana']

del fruits[0]
print(f"fruits: {fruits}")