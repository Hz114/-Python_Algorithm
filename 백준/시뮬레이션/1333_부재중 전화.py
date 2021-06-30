N, L, D = map(int, input().split())

# 초 단위로 음악 재생 상태를 저장하는 배열
time = []
for n in range(0, N):
    # 음악이 재생중일땐 1을 저장
    for l in range(0, L):
        time.append(1)
    # 음악 중간 쉬는 타임엔 0을 저장
    for r in range(0,5):
        time.append(0)

answer = D
# 배열의 크기보다 벨소리가 울리는 시간이 커지면 탈출
while answer < len(time):
    # 벨소리가 울리는 시간이 쉬는 타임이면 반복문 탈출
    if time[answer] == 0:
        break
    else:
        # 다음 벨이 울리는 시간을 확인
        answer += D

print(answer)


