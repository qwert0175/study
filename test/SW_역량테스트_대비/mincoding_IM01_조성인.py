T = int(input())
for test_case in range(1,T+1):
    N,P = map(int,input().split())
    MAP = [list(map(int,input().split())) for _ in range(N)]
    # 최대 위력 변수
    max_cure = 0

    # 2차원 배열 순회
    for i in range(N):
        for j in range(N):
            # 가운데
            center = MAP[i][j]
            # 가로
            x_cure = sum(MAP[i][max(0,j-P):min(N-1,j+P)+1])
            #  세로
            y_cure = sum([MAP[k][j] for k in range(max(0,i-P),min(N-1,i+P)+1)])
            # 십자 = 가로 + 세로 - 가운데
            cure = x_cure + y_cure - center

            # 최대치 갱신
            if max_cure < cure:
                max_cure = cure

    print(f'#{test_case} {max_cure}')