def outer():
    message = "Hello Python"

    def inner():
        print(message)

    return inner

func = outer()
func()

def make_multiplier(number):

    def multiply(value):
        return number*value

    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(10))
print(triple(10))