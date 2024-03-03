T = int(input())
for test_case in range(1,T+1):
    N,K = map(int,input().split())
    MAP = [list(map(int,input().split())) for _ in range(N)]
    count = 0

    # 맵을 순회
    for i in range(N):
        for j in range(N):
            # 빈칸을 찾았을때
            if MAP[i][j] == 1:
                # 위가 빈칸이 아닌 경우
                if i == 0 or MAP[i-1][j] == 0:
                    n = 1
                    # 아래로 빈칸을 계속 찾음
                    while i+n < N:
                        if MAP[i+n][j] == 1:
                            n += 1
                        else:
                            break
                    # n은 빈칸 개수와 동일 목표인 K와 동일하면 카운트
                    if n == K:
                        count += 1
                # 왼쪽이 빈칸이 아닌 경우
                if j == 0 or MAP[i][j-1] == 0:
                    n = 1
                    # 오른쪽으로 빈칸을 계속 찾음
                    while j+n < N:
                        if MAP[i][j+n] == 1:
                            n += 1
                        else:
                            break
                    # n은 빈칸 개수와 동일 목표인 K와 동일하면 카운트
                    if n == K:
                        count += 1

    print(f'#{test_case} {count}')