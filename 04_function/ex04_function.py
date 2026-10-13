def student_result(name, *scores):
    average = sum(scores)/len(scores)
    result = ""
    if average >= 60:
        result = "합격"
    else:
        result = "불합격"

    return name, average, result

name, average, result = student_result("Kim", 80, 90, 100)
print("이름:",name)
print("평균:",average)
print("결과:",result)