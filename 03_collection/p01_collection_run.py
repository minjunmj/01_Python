scores = [80,70,83,82,81]
total  = 0 # 합계

for score in scores:
    print(score)
    total += score

count=len(scores) # 학생 수
print(f'count:{count}')

average = total / len(scores)

print(f'합계: {total}')    
print(f'평균: {average}')