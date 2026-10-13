scores = [80, 95, 70, 85, 90]

def analyze_scores(scores):
    return sum(scores), sum(scores)/len(scores), max(scores), min(scores)

total, average, maximum, minimum = analyze_scores(scores)

print("합계:", total)
print("평균:", average)
print("최고:", maximum)
print("최저:", minimum)
