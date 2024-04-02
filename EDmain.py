num = int(input("정수 입력:"))
cnt = 0

for i in range(1, num+1, 1):
    last = i
    for j in range(1, 100, 1):
        if last <= 0.1:
                print(i, end=' ')
                break
        if (last % 10) % 3 == 0 and (last % 10) / 3 >= 1:
            print("짝", end=' ')
            cnt += 1
            break
        
        last = int(last / 10)

print(cnt)
