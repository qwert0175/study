# Python 기초문법

<br>

### list

- 여러 개의 값을 순서대로 저장하는 변경 가능한 시퀀스 자료형

- 0개 이상의 객체를 포함하며 데이터 목록을 저장

- 대괄호([])로 표기

- 데이터는 어떤 자료형도 저장할 수 있음

<br>

### list 특징

- 인덱싱

- 슬라이싱

- 길이

- 중첩된 리스트 접근

  ```
  my_list = [1,2,3,'Python',['hello','world','!!!']]

  print(len(my_list))  # 5
  print(my_list[4][-1])  # !!!
  print(my_list[-1][1][0])  # w
  ```

- 변경 가능

  ```
  my_list = [1,2,3]
  my_list[0] = 100

  print(my_list)  #[100,2,3]
  ```

<br>

### tuple

- 여러 개의 값을 순서대로 저장하는 변경 불가능한 시퀀스 자료형

- 0개 이상의 객체를 포함하며 데이터 목록을 저장

- 소괄호(())로 표기

- 데이터는 어떤 자료형도 저장할 수 있음

- 요소를 하나를 가진 튜플일 경우 ,를 넣어줘야됨

  ```
  # ,가 없으면 튜플이 안됨
  my_tuple = (1,)
  ```

<br>

### tuple 특징

- 인덱싱

- 슬라이싱

- 길이

- 변경 불가

  ```
  my_tuple = (1,'a',3,'b',5)

  # TypeError : 'tuple' object does not support item assignment
  my_tuple[1] = 'z'
  ```

<br>

### 튜플의 사용처

- 튜플의 불변 특성을 사용한 여러개의 값을 전달, 그룹화, 다중 할당 등

- 개발자가 직접 사용하기 보다 파이썬의 내부동작에서 주로 사용됨

<br>

### range

- 연속된 정수 시퀀스를 생성하는 변경 불가능한 자료형

- range(n)

  - 0부터 n-1까지의 숫자의 시퀀스

  ```
  my_range = range(5)
  print(my_range) # range(0,5)
  print(list(my_range)) # [0,1,2,3,4]
  ```

- range(n, m)

  - n부터 m-1까지의 숫자의 시퀀스

  ```
  my_range = range(1,10)
  print(my_range) # range(1,10)
  print(list(my_range)) # [1,2,3,4,5,6,7,8,9]
  ```

- 주로 반복문과 함께 사용 예정

<br>

### dict

- key - value 쌍으로 이루어진 순서와 중복이 없는 변경 가능한 자료형

- key는 변경 불가능한 자료형만 사용가능(str, int, float,tuple,range,...)

- value는 모든 자료형 사용가능

- 중괄호({})로 표기

<br>

### dict 특징

- key를 통해 value에 접근

  - 순서가 없기 때문에 index 사용 불가

- key는 변경 불가능 하지만 value는 변경 가능

- 중복불가

  ```
  # 같은 key를 사용하면 갱신됨
  my_dict = {
    'number' : 12,
    'list' : [1,2,3],
    'number' : 100
  }

  print(my_dict)  # {'number' : 100, 'list' : [1,2,3]}
  ```

### set

- 순서와 중복이 없는 변경 가능한 자료형

- 수학에서의 집합과 동일한 연산 가능

- 중괄호({})로 표기

  ```
  # 빈 set를 만들때 set()를 사용 -> {}는 dict
  my_set_1 = set()
  my_set_2 = {1,2,3}
  my_set_3 = {1,1,1}

  print(my_set_1)  # set()
  print(my_set_2)  # {1,2,3}
  print(my_set_3)  # {1}
  ```