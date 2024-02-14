def f(i,k):
    global cnt
    global min_v
    cnt += 1
    if i == k:
        s = 0
        for j in range(k):
            s += arr[j][P[j]]
        if min_v > s:
            min_v = s
    else:
        for j in range(i,k):
            P[i], P[j] = P[j], P[i]
            f(i+1, k)
            P[i], P[j] = P[j], P[i]

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
P = [i for i in range(N)]
min_v = 100
cnt = 0
f(0,N)
print(min_v,cnt)

def f2(i,k,s):
    global cnt
    global min_v
    cnt += 1
    if i == k:
        if min_v > s:
            min_v = s
    elif s >= min_v:
        return
    else:
        for j in range(i,k):
            P[i], P[j] = P[j], P[i]
            f2(i+1, k,s+arr[i][P[i]])
            P[i], P[j] = P[j], P[i]

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
P = [i for i in range(N)]
min_v = 100
cnt = 0
f2(0,N,0)
print(min_v,cnt)