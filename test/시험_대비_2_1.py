# 풍선팡

T = int(input())
for test_case in range(1, T+1):

    N,M = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]

    max_power = 0

    for i in range(N):
        for j in range(M):
            power = matrix[i][j]
            up = max(i - power, 0)
            down = min(i + power, N-1)
            left = max(j - power, 0)
            right = min(j + power, M-1)

            result = 0

            print(up,down,left,right)

            result += sum(matrix[k][j] for k in range(up,down + 1))
            result += sum(matrix[i][k] for k in range(left,right + 1))
            result -= power

            max_power = max(max_power, result)

    print(f'#{test_case} {max_power}')

# 풍선팡2

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]

    maximum = 0

    for i in range(N):
        for j in range(M):
            power = matrix[i][j]
            if i == 0:
                up = 0
            else:
                up = matrix[i-1][j]
            if i == N-1:
                down = 0
            else:
                down = matrix[i+1][j]
            if j == 0:
                left = 0
            else:
                left = matrix[i][j-1]
            if j == M-1:
                right = 0
            else:
                right = matrix[i][j+1]

            total = up + down + left + right + power

            if maximum < total:
                maximum = total

    print(f'#{test_case} {maximum}')
