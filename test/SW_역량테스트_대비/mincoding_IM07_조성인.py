T = int(input())

for test_case in range(1,T+1):
    # 사각형1
    s1 = list(map(int,input().split()))
    # 사각형2
    s2 = list(map(int,input().split()))

    # 사각형이 떨어져 있는 경우
    if s1[2] < s2[0] or s1[3] < s2[1] or s2[2] < s1[0] or s2[3] < s1[1]:
        result = 4
    # 사각형이 점으로 만나는 경우
    elif s1[0] == s2[2] or s1[2] == s2[0]:
        if s1[1] == s2[3] or s1[3] == s2[1]:
            result = 3
        # 사각형이 선으로 만나는 경우1
        else:
            result = 2
    # 사각형이 선으로 만나는 경우2
    elif s1[1] == s2[3] or s1[3] == s2[1]:
        result = 2
    # 나머지
    else:
        result = 1

    print(f'#{test_case} {result}')