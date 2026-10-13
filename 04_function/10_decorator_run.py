print("="*50)
print("데코레이터")
print("="*50)

def decorator(func):

    def wrapper():
        print("함수 실행 시작")

        func()

        print("함수 실행 종료")

    return wrapper

@decorator
def hello():
    print("Hello Python")

hello()

hello_deco = decorator(hello)
hello_deco()

