### 파리퇴치

# 테스트케이스의 개수
T = int(input())

for test_case in range(1,T+1):
    # 배열의 길이, 파리채의 크기
    N,M = map(int,input().split())
    # 2차원 배열
    matrix = [list(map(int,input().split())) for _ in range(N)]
    # 범위 내 파리의 최댓값
    max_kill = 0
    
    # 2차원 순회
    for i in range(N-M+1):
        for j in range(N-M+1):
            # 범위 내 파리
            kill = 0
            # 파리채의 행 순회
            for k in range(M):
                # 각 행의 범위 내 파리를 추가
                kill += sum(matrix[i+k][j:j+M])
            
            # 최댓값이 바뀌면 갱신
            if max_kill < kill:
                max_kill = kill

    print(f'#{test_case} {max_kill}')

### 풍선팡

# 테스트 케이스의 개수
T = int(input())

for test_case in range(1,T+1):
    # 배열의 세로, 가로 길이
    N,M = map(int,input().split())
    # 2차원 배열
    matrix = [list(map(int,input().split())) for _ in range(N)]
    # 최대 피해량
    max_pang = 0

    for i in range(N):
        for j in range(M):
            # 현재 위치의 풍선의 숫자(터지는 범위)
            power = matrix[i][j]
            # i번째 행에서의 범위만큼의 합
            x_pang = sum(matrix[i][max(j-power,0):min(j+power,M-1)+1])
            # 범위 내의 행에서 j번째 열의 합
            y_pang = sum([matrix[k][j] for k in range(max(i-power,0),min(i+power,N-1)+1)])
            # 십자 범위의 합은 가로 + 세로에서 가운데가 중첩되므로 가운데를 빼줌
            pang = x_pang + y_pang - power
            
            # 현재 피해가 최대보다 크면 갱신
            if max_pang < pang:
                max_pang = pang

    print(f'#{test_case} {max_pang}')

### 최소 배열합

# 테스트 케이스의 개수
T = int(input())

# 재귀함수(해당 행, 현재까지의 합)
def get_min(row,now_sum):
    # 변경할 최소값 전역변수 설정
    global min_sum
    # 마지막 행 : N-1, 마지막 행까지 다 돌았을 때 N
    if row == N:
        # 현재 합이 더 작다면 최소 합 변경
        if min_sum > now_sum:
            min_sum = now_sum
    else:
        # 해당 행을 순회
        for n in range(N):
            # 방문이 안되어 있으면
            if not visited[n]:
                # 방문 처리
                visited[n] = 1
                # 다음 행으로 넘어감
                get_min(row+1,now_sum + matrix[row][n])
                # 방문 처리를 되돌림
                visited[n] = 0

for test_case in range(1,T+1):
    # 배열의 길이
    N = int(input())
    # 2차원 배열
    matrix = [list(map(int,input().split())) for _ in range(N)]
    # 나올 수 있는 최대치를 최소로 설정(0~9까지의 숫자 9개 * 최대 10줄)
    min_sum = 90
    # 방문 행 처리 리스트
    visited = [0] * N
    # 재귀 함수 실행(0번째 행, 현재 합:0)
    get_min(0,0)

    print(f'#{test_case} {min_sum}')

### 스위치 켜고 끄기
    
# 스위치 개수
N = int(input())
# 스위치
switchs = list(map(int,input().split()))
# 학생 수
M = int(input())
# 학생 = [성별, 번호]
students = [list(map(int,input().split())) for _ in range(M)]

# 학생 순회
for student in students:
    # 스위치 순회
    for i in range(N):
        # 학생이 남자일 경우
        if student[0] == 1:
            # 스위치 번호가 학생 번호의 배수이면
            if (i+1) % student[1] == 0:
                # 해당 스위치를 누름
                switchs[i] = int(not switchs[i])
        
        # 남자가 아닌 경우
        else:
            # 스위치의 번호가 학생 번호와 일치하면
            if i+1 == student[1]:
                # 해당 스위치를 누르고
                switchs[i] = int(not switchs[i])
                # while문을 사용해 1칸씩 앞뒤를 같은지 비교
                n = 1
                while 0 <= i-n and i+n < N and switchs[i-n] == switchs[i+n]:
                    # 같으면 스위치를 누름
                    switchs[i-n] = int(not switchs[i-n])
                    switchs[i+n] = int(not switchs[i+n])
                    # 다음 1칸 보기
                    n += 1

# 요구사항대로 출력(20개까지 띄어쓰기, 이후 줄바꿈)
for n in range(N):
    # 인덱스 0~19번까지가 20이므로 각 19번째에서 줄바꿈
    if n % 20 == 19:
        print(switchs[n])
    else:
        print(switchs[n], end=' ')