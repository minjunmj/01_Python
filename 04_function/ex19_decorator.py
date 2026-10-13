def execution_log(func):

    def wrapper():
        print("함수 실행 시작")
        func()
        print("함수 실행 종료")

    return wrapper

@execution_log
def hello():
    print("Hello Python")

hello()