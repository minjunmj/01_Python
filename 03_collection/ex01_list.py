# print("="*50)
# print("1. 기본 인덱스 문제")
# print("="*50)

# nums = [10, 20, 30, 40, 50]

# print(nums[0])
# print(nums[-1])
# print(nums[2])

# nums = [5, 10, 15, 20, 25, 30, 35]
# print(nums[:3])
# print(nums[-3:])
# print(nums[::-1])

# nums = [1, 2, 3, 4, 5]
# nums[2]= 300
# nums[-1] = 999
# print(nums)

# data = [100, 200, 300]
# data.append(400)
# data.insert(1,150)
# print(data)

# nums = [1, 2, 3, 4, 5, 3]
# nums.remove(3)
# nums.pop(2)
# nums.pop()
# print(nums)

# nums = [2, 4, 6, 8, 10]
# total = 0
# l = []
# for i in nums:
#     total+=i
#     l.append(i*2)
# print(f"리스트: {nums}")
# print(f"모든 요소 합: {total}")
# print(f"모든 요소 2배: {l}")

# nums = [1, 2, 3, 4, 5, 6, 7, 8]
# print(f"홀수만 추출 {[x for x in nums if x%2 == 1]}")
# print(f"모든 요소의 제곱 값: {[x**2 for x in nums]}")

scores = [88, 95, 70, 100, 67, 82]
print(max(scores))
print(min(scores))
print(sum(scores)/len(scores))

