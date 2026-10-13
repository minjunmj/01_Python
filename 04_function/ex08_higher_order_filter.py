def is_even(number):
    return number%2==0

def is_over_50(number):
    return number>=50

def filter_data(numbers, func):
    return list(filter(func, numbers))

numbers = [10, 25, 30, 55, 60, 75, 80]

print(filter_data(numbers, is_even))
print(filter_data(numbers, is_over_50))

