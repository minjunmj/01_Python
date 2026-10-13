#문자열 내장 함수와 메서드

text = "I like Java"
result = text.replace("Java", "Python")
print(result)

text = "  I like Java  "
print(f"|{text.lstrip()}|") # 왼쪽 공백 제거
print(f"|{text.rstrip()}|") # 오른쪽 공백 제거
print(f"|{text.strip()}|") # 공백 제거

text = "Hello Python"
print(text.find("Python99"))

print(text.index("Python"))