# OOP(객체 지향 프로그래밍)

<br>

### 상속

- 기존 클래스의 속성과 메서드를 물려받아 새로운 하위 클래스를 생성하는 것

<br>

### 상속이 필요한 이유

- 코드 재사용
  
  - 상속을 통해 기존 클래스의 속성과 메서드를 재사용

  - 새로운 클래스를 작성할 때 기존 클래스의 기능을 그대로 활용할 수 있으며 중복된 코드를 줄일 수 있음

- 계층 구조
  
  - 상속을 통한 클래스들 간 계층 구조 형성
  
  - 부모 클래스와 자식 클래스 간의 관계 표현하고 더 구체적인 클래스를 만들 수 있음

- 유지보수
  
  - 상속을 통한 기존 클래스의 수정이 필요한 경우 해당 클래스만 수정하면 되므로 유지보수가 용이해짐

  - 코드의 일관성을 유지하고, 수정이 필요한 범위를 최소화할 수 있음

<br>

### 다중상속

- 둘 이상의 상위 클래스로부터 여러 행동이나 특징을 상속받을 수 있는 것

- 상속 받은 모든 클래스의 요소를 활용 가능

- 중복된 속성이나 메서드가 있는 경우 상속 순서에 의해 결정됨

<br>

### 다이아몬드 문제

- 두 클래스 B와 C가 A에서 상속되고, 클래스 D가 B와 C 모두에서 상속될 때 발생하는 모호함

- B와 C가 재정의한 메서드가 A에 있고 D가 이를 재정의하지 않은 경우라면

- D는 B의 메서드 중 어떤 버전을 상속하는가? 아니면 C의 메서드 버전을 상속하는가?

<br>

### 파이썬에서의 해결책

- MRO(Method Resolution Order) 알고리즘을 사용하여 클래스 목록을 생성

- 부모 클래스로부터 상속된 속성들의 검색을 깊이 우선으로, 왼쪽에서 오른쪽으로, 계층 구조에서 겹치는 같은 클래스를 두번 검색하지 않음 

- 그래서, 속성이 D에서 발견되지 않으면 B에서 찾고 거기에서도 발견되지 않으면 C에서 찾는 식으로 진행됨

<br>

### super

- super() : 부모클래스 객체를 반환하는 내장함수

- 다중 상속 시 MRO를 기반으로 현재 클래스가 상속하는 모든 부모 클래스 중 다음에 호출될 메서드를 결정하여 자동으로 호출

- 단일 상속 구조
  
  - 명시적으로 이름을 지정하지 않고 부모 클래스를 참조할 수 있으므로 코드를 더 유지 관리하기 쉽게 만들 수 있음
  - 클래스 이름이 변경되거나 부모 클래스가 교체되어도 super()를 사용하면 코드 수정이 더 적게 필요

- 다중 상속 구조
  - MRO를 따른 메서드 호출
  - 복잡한 다중 상속 구조에서 발생할 수 있는 문제를 방지

<br>

### MRO가 필요한 이유

- 부모 클래스들이 여러 번 엑세스 되지 않도록 순서를 보존하고 각 부모를 한 번만 호출하고 부모의 우선순쉬에 영향을 주지 않으면서 서브 클래스를 만드는 단조적인 구조 형성

  - 프로그래밍 언어의 신뢰성 있고 확장성 있는 클래스를 설계할 수 있도록 도움

  - 클래스 간의 메서드 호출 순서가 예측가능하게 유지되며 코드의 재사용성과 유지 보수성인 향상

<br>

### 버그

- 소프트웨어에서 발생하는 오류 또는 결함

- 프로그램의 예상된 동작과 실제 동작 사이의 불일치

<br>

### 디버깅

- 소프트웨어에서 발생하는 버그를 찾아내고 수정하는 과정

- 프로그램의 오작동 원인을 식별하여 수정하는 작업

<br>

### 디버깅 방법

- print 함수 활용

- 개발환경(text editor, IDE) 등에서 제공하는 기능 활용

- Python tutor 활용(단순 파이썬 코드인 경우)

- 뇌 컴파일 눈 디버깅 등

<br>

### 에러

- 프로그램 실행 중에 발생하는 예외 상황

- 문법에러 : 프로그램의 구문이 올바르지 않은 경우 발생

- 예외 : 프로그램 실행 중에 감지되는 에러

<br>

### 내장 예외

- 예외 상황을 나타내는 예외 클래스들

- 파이썬에 이미 정의되어 있으며, 특정 예외 상황에 대한 처리를 위해 사용

<br>

### 내장 예외 예시

- ZeroDivisionError : 0으로 나눌 때 발생

- NameError : 지역 또는 전역 이름을 찾을 수 없을 때 발생

- TypeError

  - 타입 불일치

  - 인자 누락

  - 인자 초과

  - 인자 타입 불일치

- ValueError : 연산이나 함수에 문제가 없지만 부적절한 값을 인자로 받았고 상황이 IndexError처럼 더 구체적인 예외로 설명되지 않는 경우

- IndexError : 시퀀스 범위가 인덱스를 벗어났을 때 발생

- KeyError : 딕셔너리에 해당 키가 존재하지 않는 경우

- ModuleNotFoundError : 모듈을 찾을 수 없을 때 발생

- ImportError : Import 하려는 이름을 찾을 수 없을 때 발생

- KeyboardInterrupt : 사용자가 Control + C 또는 Delete를 누를 때 발생(터미널 강제종료)

- IndentationError : 잘못된 들여쓰기

<br>

### 예외 처리

- try와 except
  
  - try 블록에 예외가 발생할 수 있는 코드
  
  - except 블록에는 예외가 발생했을 때 처리할 코드

  - 예외가 발생하면 프로그램 흐름은 try 블록을 빠져나와 해당 예외에 대응하는 except 블록으로 이동

<br>

### EAFP(Easier to Ask for Forgiveness than Permission)

- 예외 처리를 중심으로 코드를 작성하는 접근방식

- try-except

<br>

### LBYL(Look Before You Leap)

- 값 검사를 중심으로 코드를 작성하는 접근방식

- if-else

<br>

### 비교

|EAFP|LBYL|
|---|---|
|일단 실행하고 예외를 처리|실행 전에 조건을 검사|
|코드를 실행하고 예외가 발생하면 예외처리를 수행|코드 실행 전에 조건문 등을 사용하려 예외 상황을 미리 검사하고 예외 상황을 피하는 방식|
|코드에서 예외가 발생할 수 있는 부분을 미리 예측하여 대비하는 것이 아니라 예외가 발생한 후에 예외를 처리|코드가 좀 더 예측 가능한 동작을 하지만 코드가 더 길고 복잡해질 수 있음|
|예외 상황을 예측하기 어려운 경우에 유용|예외 상황을 미리 방지하고 싶을 때 유용|