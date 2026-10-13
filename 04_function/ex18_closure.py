def create_rate_limiter(limit):
    cnt = 0
    def request():
        nonlocal cnt
        cnt += 1
        if cnt > limit:
            return "요청 횟수 초과"
        return f"요청 성공 ({cnt}/{limit})"

    return request

api_request = create_rate_limiter(3)

print(api_request())
print(api_request())
print(api_request())
print(api_request())
print(api_request())