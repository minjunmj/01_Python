#### 조건

# 필기 점수가 60점 이상
# 실기 점수가 60점 이상
# 두 조건을 모두 만족하면 합격입니다
# 하나라도 만족하지 못하면 불합격입니다

written = int(input("필기점수"))
practice = int(input("실기점수"))

result = "합격입니다" if written>=60 and practice>=60 else "불합격입니다"
print(result)