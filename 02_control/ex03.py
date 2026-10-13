# 키와 몸무게를 입력 받아 BMI를 계산하고 결과를 출력하세요
# BMI 계산식:
# BMI = 몸무게(KG) / 키(m) * 키(m)

weight = int(input("몸무게"))
height = int(input("키"))
height /= 100

BMI = weight / (height**2)
# BMI = round(BMI, 2)

result = None

if BMI < 18.5:
    result = "저체중"
elif BMI < 23:
    result = "정상"
elif BMI < 25:
    result = "과체중"
else:
    result = "비만"

print(f"키(cm): {height}")
print(f"몸무게(kg): {weight}")
print(f"BMI: {BMI:.2f}")
print(f"판정: {result}")
