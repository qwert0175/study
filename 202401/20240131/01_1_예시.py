### 2차원 배열 받기

# 3
# 1 2 3
# 4 5 6
# 7 8 9

# N = int(input())
# arr1 = [list(map(int,input().split())) for _ in range(N)]

N = 3
arr1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(arr1)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

### 2차원 배열 수정

arr2 = [[0]*N for _ in range(N)]
arr3 = [[0]*N]*N  # 얕은 복사

print(arr2)  # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print(arr3)  # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

arr2[0][0] = 1
arr3[0][0] = 1  # arr3[0]을 얕은 복사했기 때문에 다 바뀜

print(arr2)  # [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
print(arr3)  # [[1, 0, 0], [1, 0, 0], [1, 0, 0]]

### 행 우선 순회

result = ''
for i in range(N):
    for j in range(N):
        result += str(arr1[i][j])

print(result)  # 123456789

### 열 우선 순회

result = ''
for j in range(N):
    for i in range(N):
        result += str(arr1[i][j])

print(result)  # 147258369

### 지그재그 순회

result = ''
for i in range(N):
    for j in range(N):
        result += str(arr1[i][j + (N - 1 - 2 * j) * (i % 2)])

print(result)  # 123654789

### 델타를 이용한 2차원 배열 탐색

# 시작 인덱스
i = 0
j = 0

di = [0,1,0,-1]
dj = [1,0,-1,0]

for k in range(4):
    ni = i + di[k]
    nj = j + dj[k]

    # 2차원 배열 안에 있는 경우에만 출력
    if 0 <= ni < N and 0 <= nj < N:
        print(arr1[ni][nj], end= ' ')

print()

### 전치행렬

# 대각선 기준으로 값 바꾸기(반전)
        
for i in range(N):
    for j in range(N):
        if i < j:
            arr1[i][j],arr1[j][i] = arr1[j][i],arr1[i][j]

print(arr1)

### 부분집합 생성 개수

bit = [0,0,0,0]
for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            for l in range(2):
                bit[3] = l
                print(bit)
