# Python 기초문법

<br>

### 프로그래밍

- 프로그램 : 명령어들의 집합

- 새 연산을 정의하고 조합해 유용한 작업을 수행하는 것

<br>

### 프로그래밍 언어

- 컴퓨터에게 작업을 지시하고 문제를 해결하는 도구

<br>

### Python

- 간결하고 읽기 쉬운 문법

- 다양한 응용분야

  - 데이터 분석, 인공지능, 웹개발, 자동화 등

- 파이썬 커뮤니티의 지원

  - 세계적인 규모의 풍부한 온라인 포럼 및 커뮤니티 생태계

<br>

### Python 프로그램의 실행

- 파이썬 인터프리터가 가용자의 명령어를 운영체제가 이해하는 언어로 바꿈

- 인터프리터 사용법

  - shell 이라는 프로그램으로 한 번에 한 명령어씩 입력해서 실행

  - 파이썬 파일에 작성된 프로그램 실행

<br>

### 표현식

- 값, 변수, 연산자 등을 조합하여 계산되고 결과를 내는 코드 구조

- 표현식이 평가되어 값이 반영됨

<br>

### 평가

- 표현식이나 문장을 실행하여 그 결과를 계산하고 값을 결정하는 과정

- 표현식이나 문장을 순차적으로 표현하여 프로그램의 동작을 결정

<br>

### 문장

- 실행가능한 동작을 기술하는 코드

- 조건문, 반복문, 함수 정의 등

<br>

### 타입

- 값이 어떤 종류의 데이터인지, 어떻게 해석되고 처리되어야 하는지 정의

- 값(피연산자)과 값들에 적용할 수 있는 연산(연산자)

<br>

### 데이터 타입

- Numeric Type : int(정수), float(실수), complex(복소수)

- Sequence Type : list, tuple, range

- Text Sequence Type : str(문자열)

- Set Type : set

- Mapping Type : dict

- 기타 : None,Boolean, Functions

<br>

### 산술 연산자

- \- : 음수부호

- \+ : 덧셈

- \- : 뺄셈

- \* : 곱셈

- / : 나눗셈

- // : 몫

- % : 나머지

- ** : 지수(거듭제곱)

<br>

### 산술연산자 우선순위

1. 지수

2. 음수부호

3. 곱셈, 뺄셈, 몫, 나머지

4. 덧셈, 뺄셈

<br>

### 변수

- 값을 참조하는 이름

- 변수명 규칙

  - 영문 알파벳, 언더스코어(_), 숫자로 구성

  - 숫자로 시작할 수 없음

  - 대소문자를 구분

  - 특정 키워드는 파이썬의 내부 예약어로 사용할 수 없음

<br>

### 할당

- 메모리의 모든 위치에 메모리를 식별하는 고유한 메모리 주소 존재

- 변수는 그 변수가 참조하는 객체의 메모리 주소를 가짐

  - 객체 : 타입을 갖는 메모리 주소 내 값

<br>

### 할당문

1. 할당연산자(=) 오른쪽에 있는 표현식을 평가해서 값(메모리 주소)을 생성

2. 값의 메모리 주소를 '=' 왼쪽에 있는 변수에 저장

    - 존재하지 않는 변수라면 새 변수를 생성

    - 존재하는 변수라면 기존변수를 재사용하여 변수에 들어있는 메모리 주소를 변경

<br>

### Style Guide

- 코드의 일관성과 가독성을 향상시키기 위한 규칙과 권장사항들의 모음(맞춤법)

- Python Style Guide(일부)

  - 변수명은 직관적인 이름 사용

  - 공백 4칸을 사용하여 코드블록 들여쓰기

  - 한줄의 길이는 79자로 제한하며, 길어질 경우 줄 바꿈을 사용

  - 문자와 밑줄(_)을 사용하여 함수, 변수, 속성의 이름을 작성

  - 함수 정의나 클래스 정의 등의 블록 사이에는 빈 줄을 추가

  - [Python Style Guide](https://peps.python.org/pep-0008)

<br>

### 주석

- 프로그램 코드 내에 작성되는 설명이나 메모

- 인터프리터에 의해 실행되지 않음

<br>

### 주석의 목적

- 코드의 특정 부분을 설명하거나 임시로 코드를 비활성화 할때

- 코드를 이해하거나 문서화하기 위해

- 다른 개발자나 자신에게 의도나 동작을 설명하는데 도움

<br>

### Data Types

- 값의 종류와 그 값에 적용가능한 연산과 동작을 결정하는 속성

- 값들을 구분하고 어떻게 다뤄야 하는지 알 수 있음

- 타입을 명시적으로 지정하면 코드를 읽는 사람이 변수의 의도를 더 쉽게 이해할 수 있고 잘못된 데이터 타입으로 인한 오류를 예방

<br>

### int

- 정수를 표현하는 자료형

- 진수 표현

  - 2진수(Binary) : 0b

  - 8진수(octal) : 0o

  - 16진수(hexadecimal) : 0x

<br>

### float

- 실수를 표현하는 자료형

- 프로그래밍 언어에서 float는 실수에 대한 근삿값

  - 무한한 값을 저장할 수 없어 사람이 사용하는 10진법의 근삿값만 표시
  
  - 값이 정확히 일치하지 않아 예상치 못한 결과가 나타나기도 함(Floating Point Rounding Error)

<br>

### Sequence Types

- 여러 개의 값들을 순서대로 나열하여 저장하는 자료형

- 순서(Sequence) : 값들이 순서대로 저장(정렬 x)

- 인덱싱(Indexing) : 각 값에 고유한 인덱스(번호)를 가지고 있으며, 인덱스를 사용하여 특정 위치의 값을 선택하거나 수정 가능

- 슬라이싱(Slicing) : 인덱스 범위를 조절해 부분적인 값을 추출할 수 있음

- 길이(Length) : len() 함수를 사용하여 저장된 값의 개수(길이)를 구할 수 있음

- 반복(lteration) : 반복문을 사용하여 저장된 값들을 반복적으로 처리할 수 있음

<br>

### str

- 문자들의 순서가 있는 변경 불가능한 시퀀스 자료형
  
- 단일 문자나 여러 문자의 조합으로 이루어짐
  
- 작은따옴표(') 또는 큰따옴표(")로 감싸서 표현

- 문자열의 일부를 바꾸는 것은 불가

<br>

### Escape Sequence

- 역슬래시(\\) 뒤에 특정 문자가 와서 특정한 기능을 사용

- 파이썬의 일반적인 문법규칙을 잠시 탈출한다는 의미

<br>

### String Interpolation(문자열 삽입)

- 문자열 내에 변수나 표현식을 삽입하는 방법

- f-string

  - 문자열에 f 또는 F 접두어를 붙이고 표현식을 {expression}로 작성하여 문자열에 파이썬 표현식의 값을 삽입할 수 있음

<br>

### Index

- 시퀀스 내의 값들에 대한 고유 번호로 각 값의 위치를 식별하는데 사용되는 숫자

<br>

### Slicing

- 시퀀스의 일부분을 선택해서 추출하는 작업

- 시작 인덱스와 끝 인덱스를 지정하여 해당 범위의 값을 포함하는 새로운 시퀀스 생성

- step을 사용하여 순서를 건너뛰거나 문자열을 뒤집을 수 있음