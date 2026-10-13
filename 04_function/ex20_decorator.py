def double_result(func):

    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)*2

    return wrapper

@double_result
def add(a, b):
    return a+b

print(add(10, 20))
print(add(5, 15))
