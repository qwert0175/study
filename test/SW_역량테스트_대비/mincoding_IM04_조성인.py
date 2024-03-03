T = int(input())
for test_case in range(1,T+1):
    N,M = map(int,input().split())
    # 답안지
    answer = list(map(int,input().split()))
    # 학생들 답
    students = [list(map(int,input().split())) for _ in range(N)]
    # 학생 전체 점수
    students_score = [0] * N

    for n in range(N):
        # 학생 개인 점수 획득
        score = [0] * (M+1)
        for m in range(M):
            # 문제가 맞다면 앞의 점수에서 +1
            if students[n][m] == answer[m]:
                score[m+1] = score[m] + 1
            # 아니라면 0점
            else:
                score[m+1] = 0
        # 개인 점수 합을 저장
        students_score[n] = sum(score)

    # 가장 높은 학생과 낮은 학생의 차 출력
    print(f'#{test_case} {max(students_score)-min(students_score)}')