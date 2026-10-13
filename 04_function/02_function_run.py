print("="*50)
print("1. 전역 변수와 지역 변수")
print("="*50)

def calculate():
	number = 10
	result = number*2
	
	print(number)
	print(result)
	
calculate()

message = "Hello Python"

def hello():
	print(f"message: {message}")

hello()

print(message)

number = 100

def test():
	number = 200
	print("함수 내부:",number)

test()

print("함수 외부:", number)

tax_rate = 0.1

def calculate_tax(price):
	tax = price * tax_rate
	return tax

print(calculate_tax(100_000))