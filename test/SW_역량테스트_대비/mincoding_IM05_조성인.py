import math
T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    MAP = [list(map(int,input().split())) for _ in range(N+1)]
    # 중계기로부터 각 집에 대한 거리 리스트
    r_list = []

    # 중계기 좌표 구하기
    stop = False
    for i in range(N+1):
        for j in range(N+1):
            if MAP[i][j] == 2:
                stop = True
                break
        if stop:
            break
    
    # 각 집들의 거리 구해서 리스트에 넣기
    for k in range(N+1):
        for l in range(N+1):
            if MAP[k][l] == 1:
                r_list.append(((i-k)**2 + (j-l)**2)**(1/2))

    # 리스트에서 가장 먼 거리를 올림함
    print(f'#{test_case} {math.ceil(max(r_list))}')