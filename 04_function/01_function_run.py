print("="*50)
print("함수(Function)")
print("="*50)

def print_score(score):
    print("학생 점수:", score)

print_score(90)
print_score(80)
print_score(95)

def introduce(name, age):
    print("이름:", name)
    print("나이:", age)

introduce("PCWK", 22)

introduce(age = 21, name="pcwk")

def add_args(*args):
    print(args)
    print(type(args))
    return sum(args)

print(add_args(15, 17, 20))

def student_average(name, *scores):
    average = sum(scores)/len(scores)

    return name, average

name, average = student_average('Kim', 80, 90, 100)

print("이름:", name)
print("평균:", average)

def user_info(**kwargs):
    print(kwargs)
    print(type(kwargs))

user_info(name="Kim", age=21, grade="VIP")

def user_info(name, *scores, **kwargs):
    print("이름:", name)
    print("점수:", scores)
    print("추가정보:", kwargs)

user_info("Kim",80,90,100,age=21,grade="VIP")