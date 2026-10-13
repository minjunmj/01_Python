print("="*50)
print("1~10에서 3의 배수만 건너뛰기.")
print("="*50)

for i in range(1,11):
    if i % 3 == 0:
        continue
    
    print(i,end=' ')