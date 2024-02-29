# Binary Counting으로 부분집합 구하기

arr = ['A','B','C',]
n = len(arr)

def get_sub(tar):
    for i in range(n):
        if tar & 0x1:
            print(arr[i],end=' ')
        tar >>= 1

for tar in range(1 << n):
    print('{',end=' ')
    get_sub(tar)
    print('}')

# 도전과제(경우의 수의 개수 구하기)

arr = ['A','B','C','D','E']
n = len(arr)
cnt = 0

def get_sub(tar):
    global cnt
    friend = 0
    for _ in range(n):
        if tar & 0x1:
            friend += 1
        tar >>= 1
    if friend >= 2:
        cnt += 1

for tar in range(1 << n):
    get_sub(tar)

print(cnt)