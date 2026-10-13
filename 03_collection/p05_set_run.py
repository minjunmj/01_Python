numbers = set([10, 20, 30])
print(f"numbers: {numbers}, type: {type(numbers)}")

data = set()
print(type(data))

data = {}
print(type(data))

numbers = [10, 20, 20, 30, 30, 30]
print(type(numbers))
result = set(numbers)
print(result)

numbers = [10, 20, 20, 30, 30, 30]
print(type(numbers))

# 리스트로 다신 반환할 수도 있습니다
result = list(set(numbers))

print (result)

fruits = {'사과', '배'}
fruits.add('딸기')

print(fruits)

fruits = {'사과', '배'}
fruits.discard('사과')

print(fruits)

A = {1,2,3,4}
B = {3,4,5,6}

print(f"합집합: {A | B}")
print(f"합집합: {A.union(B)}")