def add_bonus(score):
    return score+5

def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
    
def process_scores(scores, func):
    return list(map(func, scores))
    
scores = [95, 80, 70, 60]

print(process_scores(scores, add_bonus))
print(process_scores(scores, get_grade))