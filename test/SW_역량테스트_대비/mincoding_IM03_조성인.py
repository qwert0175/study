T = int(input())
for test_case in range(1,T+1):
    N,K = map(int,input().split())
    # 샘플코드
    Sample = list(map(int,input().split()))
    # 패스코드
    PassCode = list(map(int,input().split()))

    # 샘플코드 순회
    for n in range(N):
        # 순회중 패스코드가 다 빠지면 종료
        if not PassCode:
            break

        # 샘플코드가 패스코드의 앞자리와 일치하면
        if Sample[n] == PassCode[0]:
            # 패스코드를 하나씩 뺌
            PassCode.pop(0)

    # 샘플코드 순회 종료 후 패스코드가 남아있으면 0 아니면 1
    if PassCode:
        result = 0
    else:
        result = 1

    print(f'#{test_case} {result}')