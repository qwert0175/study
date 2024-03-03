T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    MAP = [list(map(int,input().split())) for _ in range(N)]
    # 최대 사각형 넓이 변수
    max_square = 0
    # 사각형 개수 변수
    count = 0

    # 2차원 배열 순회(시작점 찾기)
    for i in range(N):
        for j in range(N):
            # 시작점을 찾았을 때 만들 수 있는 가장 큰 사각형이 최대 넓이보다 작으면 볼 필요가 없음
            if (N-i) * (N-j) < max_square:
                continue
            # 2차원 배열 순회(끝점 찾기)
            for k in range(i,N):
                for l in range(j,N):
                    # 양쪽의 값이 같을때
                    if MAP[i][j] == MAP[k][l]:
                        # 사각형의 넓이 구하기
                        square = (k-i+1) * (l-j+1)
                        # 최댓값 갱신
                        if max_square < square:
                            max_square = square
                            count = 1
                        # 최댓값과 같다면 카운트 +1
                        elif max_square == square:
                            count += 1

    print(f'#{test_case} {count}')