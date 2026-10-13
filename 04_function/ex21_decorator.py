import time


def timer(func):

    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"실행 시간: {end-start:.4f}초")
        return result
    
    return wrapper

@timer
def calculate():
    total = 0
    for i in range(1, 1000001):
        total += i

    return total

print("결과:", calculate())

