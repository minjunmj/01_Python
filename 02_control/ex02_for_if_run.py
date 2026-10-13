print("="*50)
print("1. 1~30에서 3의 배수의 합계를 출력하세요")
print("="*50)

total = 0
for i in range(3, 31, 3):
	total+=i

print(total)

print("="*50)
print("1. 문자열에서 모음 찾기")
print("="*50)

word = "Python Programing" # aeiou
list = ['a','e','i','o','u']
for i in word:
	if i.lower() in list:
		print(i)