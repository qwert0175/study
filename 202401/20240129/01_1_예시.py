### 회전 시 낙하거리

N = 9
arr = [7,4,2,0,0,6,0,7,0]
falling = 0
for i in range(N):
    cnt = 0
    for j in range(i+1, N):
        if arr[i] > arr[j]:
            cnt = cnt + 1
    if falling < cnt:
        falling = cnt
print(falling)

### 버블 정렬

N = 6  # 길이
arr = [7,2,5,3,1,4]

for i in range(N-1, 0, -1):
    for j in range(i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(arr)

### 버블 정렬(내림차 순)

N = 6  # 길이
arr = [7,2,5,3,1,4]

for i in range(N-1, 0, -1):
    for j in range(i):
        if arr[j] < arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(arr)