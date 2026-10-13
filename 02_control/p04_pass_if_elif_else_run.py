print("="*50)
print("성적을 입력 받아 학점 출력")
print("="*50)

score = int(input('성적을 입력 하세요: '))

print(f'score:{score}')

if score >= 90:
    print('A 학점')
elif score >= 80:
    pass         # 나중에 구현
elif score >=70:
    print('C 학점')    
elif score >=60:
    print('D 학점')
else:
    print('F 학점')