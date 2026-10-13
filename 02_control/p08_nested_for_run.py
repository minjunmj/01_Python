print("="*50)
print("중첩 for문")
print("="*50)

for dan in range(2,10):
    print(f"--- {dan}단 ---")
    for i in range(1,10):
        print(f"{dan} * {i} = {dan * i}")


for i in range(1,6):
    print("*"*i)