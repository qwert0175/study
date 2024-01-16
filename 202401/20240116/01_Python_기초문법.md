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

<br>

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

<br>

### set 특징

- 집합연산

  ```
  my_set_1 = {1,2,3}
  my_set_2 = {3,6,9}

  # 합집합
  print(my_set_1 | my_set_2)  # {1,2,3,6,9}

  # 차집합
  print(my_set_1 - my_set_2)  # {1,2}

  # 교집합
  print(my_set_1 & my_set_2)  # {3}
  ```

<br>

### None

- 파이썬에서 '값이 없음'을 표현하는 자료형
  ```
  variable= None
  print(variable)  # None
  ```

<br>

### Boolean

- 참(True)과 거짓(False)을 표현하는 자료형
  ```
  bool_1 = True
  bool_2 = False

  print(bool_1)  # True
  print(bool_2)  # False
  print(3 > 1)  # True
  print('3'!=3)  # True
  ```

<br>

### Collection

- 여러개의 항목 또는 요소를 담는 자료 구조
  
  |컬렉션|변경가능여부|순서여부|
  |---|---|---|
  |str|X|O|
  |list|O|O|
  |tuple|X|O|
  |set|O|X|
  |dict|O|X|

<br>

### Type Conversion

- 암시적 형변환

- 명시적 형변환

<br>

### 암시적 형변환

- 파이썬이 자동으로 형변환을 하는 것

- Boolean과 Numeric Type에서만 가능

  ```
  print(3 + 5.0)  # 8.0
  print(True + 3)  # 4
  print(True + False)  # 1
  ```

<br>

### 명시적 형변환 예시

- str -> integer : 형식에 맞는 숫자만 가능

- integer -> str : 모두 가능
  ```
  print(int('1'))  # 1
  print(str(1) + '등')  # 1등
  print(float('3.5'))  # 3.5
  print(int(3.5))  # 3

  # ValueError: invalid literal for int() with base 10: '3.5'
  print(int('3.5))
  ```

<br>

### 연산자

- 산술 연산자

  |기호|내용|
  |---|---|---|
  |+|덧셈|
  |-|뺄셈|
  |*|곱셈|
  |/|나눗셈|
  |//|몫|
  |%|나머지|
  |**|지수(거듭제곱)|

- 복합 연산자 : 연산과 할당이 함께 이루어짐

  |기호|예시|의미|
  |---|---|---|
  |+=|a += b|a = a + b|
  |-=|a -= b|a = a - b|
  |*=|a *= b|a = a * b|
  |/=|a /= b|a = a / b|
  |//=|a //= b|a = a // b|
  |%=|a %= b|a = a % b|
  |**=|a **= b|a = a ** b|

- 비교 연산자
  
  |기호|내용|
  |---|---|---|
  |<|미만|
  |<=|이하|
  |>|초과|
  |>=|이상|
  |==|같음|
  |!=|같지 않음|
  |is|같음|
  |is not|같지 않음|
  
  - is 비교 연산자

    - 메모리 내에서 같은 객체(주소)를 참조하는지 확인

    - ==는 동등성(equality), is는 식별성(identity)

    - 값을 비교하는 ==와 다름

    - is 연산자는 되도록이면 None, True, False 등을 비교할 때 사용

- 논리 연산자

  - and(논리곱) : 두 피연산자가 모두 True일 경우에만 전체 표현식을 True로 평가

  - or(논리합) : 두 피연산자 중 하나라도 True일 경우 전체 표현식을 True로 평가

  - not(논리부정) : 단일 피연산자를 부정

  ```
  print(True and False)  # False
  print(True or False)  # True
  print(Not True)  # False
  print(Not 0)  # True
  ```

  - 단축평가 : 논리연산에서 두번째 피연산자를 평가하지 않고 결과를 결정하는 동작
    
    - and : 앞이 False일 경우 뒤의 결과와 상관없이 False
    
    - or : 앞이 True일 경우 뒤의 결과와 상관없이 True

- 멤버십 연산자

  - 특정 값이 시퀀스나 다른 컬렉션에 속하는지 여부를 확인

  - in : 왼쪽 피연산자가 오른쪽 피연산자의 시퀀스에 속하는지를 확인

  - not in : 왼쪽 피연산자가 오른쪽 피연산자의 시퀀스에 속하지 않는지를 확인

- 시퀀스형 연산자

  - +와 *는 시퀀스간 연산에서 산술 연산자일때와 다른 역할을 가짐

  - \+ : 결합 연산자

  - \* : 반복 연산자