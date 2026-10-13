def add(a,b):
    return a+b

result = add(15,17)

print(f"result: {result}")

add_new = lambda a,b: a+b

print(type(add_new))
print(add_new(15,17))

