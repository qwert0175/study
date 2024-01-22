# 1번
numbers = [1,2,3,4,5]
result = 0

for num in numbers:
    if num % 2 == 0:
        continue
        result += num
    else:
        result += num * 2

print(result)  # 18

# 2번
x, y, *res = [1,2,3,4,5]
print(res)  # [3, 4, 5]

# 3번
numbers = [0,0,0,0,0]
print(numbers)  # [0,0,0,0,0]

numbers = [0] * 5
print(numbers)  # [0,0,0,0,0]

numbers = []
numbers.append(0*5)
print(numbers)  # [0]

numbers = [0 for i in range(5)]
print(numbers)  # [0,0,0,0,0]

# 4번
print(not 'True')  # False

# 5번
for char in 'ssafy':
    if  char == 's':
        print('yes!')
        break
    else:
        print('no!')
        print('next!')

print('end!')

# yes! end!

# 6번
cities = ['Seoul', 'Paris', 'London', 'Newyork']
print(cities[-3][0] + cities[-1][3])  # Py

# 7번
print(2 * 22 ** 2 + 2)  # 10

# 8번 시퀀스 타입 찾기
'''
1. set
2. dic
3. range
4. boolean
'''
# range

# 9번
my_string = 'i need python book'
new_string = ''

for idx, char in enumerate(my_string):
    if idx % 2 == 0:
        new_string += str(idx)
    else:
        new_string += char

print(new_string)  # 0 2e4d6p8t10o12 14o16k

# 10번
def func(input1, *args, **kwargs):
    total = 0
    for i in args:
        total += i * 100
    return input1 + total + kwargs['input2']

num1, *num_list, num2 = range(3, 8)
result = func(num1, *num_list, input2 = num2)
print(result)  # 1510

# 11번 파이썬 내장 함수인 'enumerate' 함수에 대한 올바른 설명
# 순회가능한(iterable) 자료형(리스트, 튜플, 문자열 등)을 입력으로 받아 인덱스와 값을 포함하는 enumerate 객체를 반환

# 12번
my_string = 'Hello world~'
substring = my_string[7:]
print(substring)  # orld~

# 13번
def my_function(x):
    return x ** 2

result = my_function(4) + my_function(3)
print(result)  # 25

# 14번
my_dict = {'apple' : 1, 'banana' : 2, 'cherry' : 3}
result = 1 in my_dict
print(result)

# False

# 15번
x = 15
y = 10
result = x > y
print(result)  # False

# 16번 파이썬 파일 확장자
# .py

# 17번 pass의 역할
# 반복문 혹은 함수의 빈 구현을 일시적으로 처리할 때 사용한다.

# 18번 fib(0)과 fib(1)이 각각 얼마나 호출되는지
def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
print(fib(4))

# fib(0) -> 2
# fib(1) -> 3

# 19번 
x = 10
y = '5'
result = x + y
print(result)  # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# 20번
dust = 90
if dust > 150:
    print('매우나쁨')
elif dust > 30:
    print('보통')
elif dust > 80:
    print('나쁨')
else :
    print('좋음')

# 보통

# 21번
lst = [range(5), range(1,5)]
map_lst = map(lambda x, y : x + y, *lst)
total = sum(map_lst)
print(total)  # 16

# 22번 Ⓐ에 들어갈 함수
string_numbers = ['1','2','3','4','5']
total = Ⓐ(int, string_numbers)
print(total) # 15

# 23번
print(11 or 7)  # 11

# 24번 Ⓐ에 들어갈 단어
Ⓐ random
lotto = random.sample(range(1,46),45)
print(lotto)

# 25번
# 횟수가 불명확한 반복에서 사용하거나 특정조건에 따라 반복을 종료 해야 할때 주로 사용하는 반복문
# while

# 26번 print의 호출 횟수
alphabet = ['A', 'B', 'C']
numbers = [1, 2, 3]
chars = ['!', '~', '.']

for alph in alphabet:
    for num in numbers:
        for char in chars:
            print(alph, num, char)
# 27회

# 27번
# 함수는 필요한 경우 결과를 return 문을 통해 반환할 수 있는데 return 문을 안 쓰면 어떤 결과가 나오는지
# None

# 28번
my_value = 3
my_value **= 2
print(my_value)  # 9

# 29번
my_list = "welcome to my home"
print(my_list[1:6])  # elcom

# 30번
x = 10
def funcA():
    x = 5
    def funcB(arg):
        x = 7
        return arg + 3
    x = funcB
    print(x)

funcA()  
# 8

# 31번 결과와 이유
print(3.0 + 2)  # 5.0, 파이썬 자동 형변환으로 int 타입을 float 타입으로 바꿔 float 타입의 연산의 결과값인 5.0으로 나옴

# 32번 range 객체 안의 요소들을 확인하려면 어떤 방법을 써야 하는가
my_list = range(1,11)
print(my_list)  # range(1,11)
# print(list(my_list))