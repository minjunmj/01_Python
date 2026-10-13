# 문자열 선언

print("="*50)
print("01. 문자열 선언")
print("="*50)

name = "이상무"
language = "Python"
message = """ Hello Python """

print(name)
print(language)
print(message)

message = '그는 "Python"을 공부합니다'
print(message)

print("="*50)
print("02. 이스케이프 문자")
print("="*50)

print("Python\nJava")
print("이름\t나이")
print("이상무\t21")
print("C:\\AI_CAMP_20260921\\01_PYTHON\\WORKSPACE")

print("="*50)
print("03. 문자열 연결하기")
print("="*50)

first_name = "상무"
last_name = "이"

name = last_name + first_name
print(name)

print("="*50)
print("04. 문자열 반복하기")
print("="*50)

message = "Python "
print(message * 3)

print("="*50)
print("04. 문자열 포맷팅")
print("="*50)

print("이름:%s" %"Tom")

name = "이상무"
age = 21

print(f"이름은 {name}이고 나이는 {age}입니다")
price = 10_000
quantity = 3

print(f"가격: {price}원")
print(f"수량: {quantity}개")
print(f"총 금액: {price * quantity}원")
name = "Python"
print(f"대문자: {name.upper()}")
pi = 3.141592
print(f"PI: {pi:.2f}")
price = 1_234_567.89
print(f"가격: {price:,.1f}원")
name = "Python"

print(f"|{name:<10}|") # 왼쪽 정렬
print(f"|{name:^10}|") # 가운데 정렬
print(f"|{name:>10}|") # 오른쪽 정렬

