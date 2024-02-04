# 임의의 카드 6장
import random

numbers = list(range(10))
deck = [number for number in numbers for _ in range(4)]

hand = random.sample(deck, 6)

print(hand)

# 테스트용
# hand = [9,7,7,5,7,8]

# 숫자 카운트용 리스트 생성
counts = [0] * 10

# 카드의 숫자를 리스트에 카운트
for i in hand:
    counts[i] += 1

print(counts)

# 베이비진 조건 변수
triplet = 0
run = 0

# 카운트 리스트를 순회
for i in range(10):

    # 카운트가 3 이상일 경우 카운트를 3개 제거하고 triplet 1 증가
    if counts[i] >= 3:
        counts[i] -= 3
        triplet += 1
        continue

    # 숫자 3개가 연속으로 1개 이상 카운트 되어 있을 경우 3 숫자의 카운트를 1개 제거하고 run 1증가
    if i < 8 and counts[i] >= 1 and counts[i+1] >= 1 and counts[i+2] >= 1:
        counts[i] -= 1
        counts[i+1] -= 1
        counts[i+2] -= 1
        run += 1
        continue

# 베이비진의 조건을 만족한다면 baby gin을 출력
if run + triplet == 2:
    print('baby gin')
else:
    print('lose')