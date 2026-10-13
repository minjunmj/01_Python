import random

print("="*50)
print("1~10사이 컴퓨터가 정한 숫자를 맞히는 게임")
print("="*50)

answer = random.randint(1,10)

while True:
    num = int(input("1~10 숫자를 입력하세요: "))
    if(num==answer):
        print("정답입니다")
        break
    if num < answer:
        print("더 큰 숫자입니다")
    else:
        print("더 작은 숫자입니다")

