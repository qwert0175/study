N = 6
K = 9
data = [7,2,4,5,2,3]  # 0~9, K=9
counts = [0] * (K+1)
temp = [0] * N

# counts 배열에 기록하기
for x in data:
    counts[x] += 1

print(counts)

# counts 누적합 구하기
for i in range(1,K+1):
    counts[i] = counts[i-1] + counts[i]

print(counts)

# data의 마지막 원소부터 정렬하기
for i in range(N-1, -1, -1):  # N-1 -> 0번 인덱스
    counts[data[i]] -= 1  # 개수를 인덱스로 변환(남은 인덱스)
    temp[counts[data[i]]] = data[i]

print(temp)

# num = 233345
num = 123456
c = [0] * 12

for i in range(6):
    c[num % 10] += 1
    num //= 10

i = 0
tri = run = 0
while i < 10:
    if c[i] >= 3:
        c[i] -= 3
        tri += 1
        continue
    if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1:
        c[i] -= 1
        c[i+1] -= 1
        c[i+2] -= 1
        run += 1
        continue
    i += 1

if run + tri == 2: print('Baby Gin')
else: print('Lose')