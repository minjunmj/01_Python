print("="*50)
print("None")
print("="*50)

result = None

print(result)
print(type(result))

print(f"result: {result}")
print(f"result type: {type(result)}")

if result is None:
	print("아직 결과가 없습니다")
	
result = "고양이"

if result is not None:
	print(f"예측 결과: {result}")