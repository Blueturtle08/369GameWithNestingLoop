print("369게임에 오신 것을 환영합니다\n숫자에 3, 6, 9가 포함되어있으면 \'짝\'이 출력됨니다")
num = int(input("정수 입력: "))
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

print("\n짝이 나온 횟수: %d" % cnt)
