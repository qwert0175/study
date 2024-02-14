def f(i, k, t):
    if i == k:
        ss = 0
        for j in range(k):
            if bit[j]:
                ss += A[j]
        # print(ss)
        if ss == t:
            for j in range(k):
                if bit[j]:
                    print(A[j], end=' ')
            print()
    else:
        for j in range(1,-1,-1):
            bit[i] = j
            f(i+1,k,t)
        # bit[i] = 1
        # f(i+1,k)
        # bit[i] = 0
        # f(i+1,k)

N = 10
A = [1,2,3,4,5,6,7,8,9,10]
bit = [0] * N
f(0,N,10)

def f2(i, k, s, t):
    global cnt
    cnt += 1
    if s == t:
        for j in range(k):
            if bit[j]:
                print(A[j], end=' ')
        print()
    elif i == k:
        return
    elif s > t:
        return
    else:
        # for j in range(1,-1,-1):
        #     bit[i] = j
        #     f(i+1,k,t)
        bit[i] = 1
        f2(i+1,k,s+A[i],t)
        bit[i] = 0
        f2(i+1,k,s,t)

N = 10
A = [1,2,3,4,5,6,7,8,9,10]
bit = [0] * N
cnt = 0
f2(0,N,0,1)
print('cnt :',cnt)