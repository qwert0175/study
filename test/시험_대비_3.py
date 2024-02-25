import math

# 공의 총 개수(흰공 포함)
N = int(input())

# 공 목록(흰공 포함)
balls = [list(map(float,input().split())) for _ in range(N)]
holes = [[0, 0], [0, 127], [127, 0], [127, 127], [254, 0], [254, 127]]
# 반지름
r = 5.73/2

# 점과 점 사이의 거리와 각도
def get_dis_arc(point_a,point_b):
    dis_x = point_b[0] - point_a[0]
    dis_y = point_b[1] - point_a[1]
    dis_ab = math.sqrt(math.pow(dis_x,2)+math.pow(dis_y,2))
    arc_A = math.degrees(math.atan2(dis_y, dis_x))
    return dis_ab, arc_A

# 점에서 각도로 거리만큼 떨어져 있는 곳의 x,y좌표
def get_xy(point,distance,arc):
    dis_x = distance * math.cos(math.radians(arc))
    dis_y = distance * math.sin(math.radians(arc))
    x = point[0] - dis_x
    y = point[1] - dis_y
    return [x,y]

# 목적구들을 순회
for i in range(1,len(balls)):
    ball = balls[i]
    # 홀을 순회해서 목적구를 기준으로 흰공 반대편에 있는 홀을 목표로 하고 반복문 종료
    for hole in holes:
        if ball[0] >= balls[0][0] and ball[1] >= balls[0][1]:
            if hole[0] >= ball[0] and hole[1] >= ball[1]:
                break
        elif ball[0] < balls[0][0] and ball[1] >= balls[0][1]:
            if hole[0] < ball[0] and hole[1] >= ball[1]:
                break
        elif ball[0] >= balls[0][0] and ball[1] < balls[0][1]:
            if hole[0] >= ball[0] and hole[1] < ball[1]:
                break
        else:
            if hole[0] < ball[0] and hole[1] < ball[1]:
                break
    
    # 몇번째 목적구
    print(i)
    # 목적구와 홀 사이의 거리와 각도
    distance,arc_A = get_dis_arc(ball,hole)
    print(distance,arc_A)
    # 흰공이 가야할 목표지점
    target_point = get_xy(hole,distance+2*r,arc_A)
    print(target_point)
    # 흰공이 가야할 거리와 각도
    distance,arc_A = get_dis_arc(balls[0],target_point)
    print(distance,arc_A)
    # 목표지점과 목적구와의 거리 재확인(약간의 오차는 있으나 공의 지름인 5.73에 근접)
    distance, arc_A = get_dis_arc(ball, target_point)
    print(distance, arc_A)