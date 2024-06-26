# Reference type

<br>

### 함수(Function)

- 참조 자료형에 속하며 모든 함수는 Function object

- 함수 구조

    - function 키워드

    - 함수의 이름

    - 함수의 매개변수

    - 함수의 body를 구성하는 statements

    - return

<br>

### 함수 정의 방법

- 선언식

    - 익명함수 사용 불가능

    - 호이스팅 있음

- 표현식

    - 함수 이름이 없는 익명함수를 사용할 수 있음

    - 선언식과 달리 표현식으로 정의한 함수는 호이스팅 되지 않으므로 함수를 정의하기 전에 먼저 사용할 수 없음

    - 표현식 사용 권장

<br>

### 매개변수

- 기본 함수 매개변수

    - 전달하는 인자가 없거나 undefined가 전달될 경우 이름 붙은 매개변수를 기본값으로 초기화

- 나머지 매개변수

    - 임의의 수의 인자를 배열로 허용하여 가변 인자를 나타내는 방법

    - 함수 정의 시 나머지 매개변수는 하나만 작성할 수 있음

    - 나머지 매개변수는 함수 정의에서 매개변수 마지막에 위치해야 함

<br>

### 매개변수와 인자 개수가 불일치 할 때

- 매개변수 개수 > 인자 개수

    - 누락된 인자는 undefined로 할당

- 매개변수 개수 < 인자 개수

    - 초과 입력한 인자는 사용하지 않음

<br>

### 전개 구문(Spread syntax)

- '...'

- 배열이나 문자열과 같이 반복 가능한 항목을 펼치는 것(확장, 전개)

- 전개 대상에 따라 역할이 다름

    - 배열이나 객체의 요소를 개별적인 값으로 분리하거나 다른 배열이나 객체의 요소를 현재 배열이나 객체에 추가하는 등

<br>

### 전개 구문 활용처

- 함수와의 사용

    - 함수 호출 시 인자 확장

    - 나머지 매개변수(압축)

- 객체와의 사용

- 배열과의 사용

<br>

### 화살표 함수

- 화살표 함수 표현식

- 함수 표현식의 간결한 표현법

- 작성 과정

    1. function 키워드 제거 후 매개변수와 중괄호 사이에 화살표 작성

    2. 매개변수가 하나라면 매개변수의 '()' 제거 가능

    3. 함수 본문의 표현식이 한 줄이라면 '{}' 및 'return' 제거 가능

<br>

### 객체(Object)

- 키로 구분된 데이터 집합을 저장하는 자료형

- 객체 구조

    - 중괄호를 이용해 작성

    - 중괄호 안에는 key: value 쌍으로 구성된 속성을 여러 개 작성 가능

    - key는 문자형만 허용

    - value는 모든 자료형 허용

<br>

### 속성 참조

- 점(.) 또는 대괄호로 객체 요소에 접근

- key 이름에 띄어쓰기 같은 구분자가 있으면 대괄호 접근만 가능

<br>

### in 연산자

- 속성이 객체에 존재하는지 여부를 확인

<br>

### Method

- 객체 속성에 정의된 함수

- object.method() 방식으로 호출

- 메서드는 객체를 행동할 수 있게 함

<br>

### this

- 객체 속성에 정의된 함수

- this 키워드를 통해 객체에 대한 특정한 작업을 수행할 수 있음

- 함수나 메서드를 호출한 객체를 가리키는 키워드

- 함수 내에서 객체의 속성 및 메서드에 접근하기 위해 사용

- javascript에서 this는 함수를 호출하는 방법에 따라 가리키는 대상이 다름

    - 단순 호출 : 전역 객체

    - 메서드 호출 : 메서드를 호출한 객체

<br>

### JavaScript this 정리

- JavaScript의 함수는 호출될 때 this를 암묵적으로 전달받음

- JavaScript에서 this는 함수가 호출되는 방식에 따라 결정되는 현재 객체를 나타냄

- Python의 self와 Java의 this가 선언 시 이미 값이 정해지는 것에 비해 JavaScript의 this는 함수가 호출되기 전까지 값이 할당되지 않고 호출 시에 결정됨(동적 할당)

    - 장점 : 함수를 하나만 만들어 여러 객체에서 재사용 가능

    - 단점 : 이런 유연함이 실수로 이어질 수 있음

<br>

### 추가 객체 문법

- 단축 속성

    - 키 이름과 값으로 쓰이는 변수의 이름이 같은 경우 단축 구문을 사용할 수 있음

- 단축 메서드

    - 메서드 선언 시 function 키워드 생략 가능

- 계산된 속성

    - 키가 대괄호로 둘러싸여 있는 속성

    - 고정된 값이 아닌 변수 값을 사용할 수 있음

- 구조 분해 할당

    - 배열 또는 객체를 분해하여 객체 속성을 변수에 쉽게 할당할 수 있는 문법

    - 함수의 매개변수로 객체 구조 분해 할당 활용 가능

- Object with '전개 구문'

    - 객체 복사(객체 내부에서 객체 전개)

    - 얕은 복사에 활용 가능

- 유용한 객체 메서드

    - Object.keys()

    - Object.values()

- Optional chaining('?.')

    - 속성이 없는 중첩 객체를 에러 없이 접근할 수 있는 방법

    - 만약 참조 대상이 null 또는 undefined라면 에러가 발생하는 것 대신 평가를 멈추고 undefined를 반환

    - 장점

        - 참조가 누락될 가능성이 있는 경우 연결된 속성으로 접근할 때 더 짧고 간단한 표현식을 작성할 수 있음

        - 어떤 속성이 필요한지에 대한 보증이 확실하지 않은 경우에 객체의 내용을 보다 편리하게 탐색할 수 있음

    - 주의사항

        - 존재하지 않아도 괜찮은 대상에만 사용해야 함

        - Optional chaining 앞의 변수는 반드시 선언되어 있어야 함

<br>

### JSON

- JavaScript Object Notation

- Key-Value 형태로 이루어진 자료 표기법

- JavaScript의 Object와 유사한 구조를 가지고 있지만 JSON은 형식이 있는 문자열

- JavaScript에서 JSON을 사용하기 위해서는 Object 자료형으로 변경해야 함

<br>

### new 연산자

```
new constructor[([arguments])]
```

- 사용자 정의 객체 타입을 생성

- 매개변수

    - constructor : 객체 인스턴스의 타입을 기술(명세)하는 함수

    - arguments : constructor와 함께 호출될 값 목록

<br>

### 배열(Array)

- 순서가 있는 데이터 집합을 저장하는 자료구조

- 배열 구조

    - 대괄호를 이용해 작성

    - 요소 자료형 : 제약 없음

    - length 속성을 사용해 배열에 담긴 요소가 몇 개인지 알 수 있음

<br>

### 주요 배열 메서드

- push() : 배열 끝에 요소를 추가

- pop() : 배열 끝 요소를 제거하고 제거한 요소를 반환

- unshift() : 배열 앞에 요소를 추가

- shift() : 배열 앞 요소를 제거하고 제거한 요소를 반환

<br>

### Array Helper Methods

- 배열 조작을 보다 쉽게 수행할 수 있는 특별한 메서드 모음

- ES6에 도입

- 배열의 각 요소를 순회하며 각 요소에 대해 함수(콜백함수)를 호출

- 메서드 호출 시 인자로 함수(콜백함수)를 받는 것이 특징

<br>

### 콜백 함수

- 다른 함수에 인자로 전달되는 함수

- 외부 함수 내에서 호출되어 일종의 루틴이나 특정 작업을 진행

<br>

### 주요 Array Helper Methods

- forEach()

    - 배열 내의 모든 요소 각각에 대해 함수(콜백함수)를 호출

    - 반환 값 없음

- map()

    - 배열 내의 모든 요소 각각에 대해 함수(콜백함수)를 호출

    - 함수 호출 결과를 모아 새로운 배열을 반환

<br>

### forEach()

- 배열의 각 요소를 반복하며 모든 요소에 대해 함수를 호출

```
arr.forEach(callback(item[, index[, array]]))
```

- 콜백함수는 3가지 매개변수로 구성

    - item : 처리할 배열의 요소

    - index : 처리할 배열 요소의 인덱스(선택인자)

    - array : forEach를 호출한 배열(선택인자)

- 반환값 : undefined

<br>

### map()

- 배열의 모든 요소에 대해 함수를 호출하고 반환된 호출 결과 값을 모아 새로운 배열을 반환

```
arr.map(callback(item[, index[, array]]))
```

- forEach 매개변수와 동일

- 반환값 : 배열의 각 요소에 대해 실행한 callback의 결과를 모은 새로운 배열

<br>

### 배열 순회 종합

- for loop

    - 배열의 인덱스를 이용하여 각 요소에 접근

    - break, continue 사용 가능

- for...of

    - 배열 요소에 바로 접근 가능

    - break, continue 사용 가능

- forEach

    - 간결하고 가독성이 높음

    - callback 함수를 이용하여 각 요소를 조작하기 용이

    - break, continue 사용 불가능

<br>

### 기타 Array Helper Methods

- filter

    - 콜백 함수의 반환 값이 참인 요소들만 모아서 새로운 배열을 반환

- find

    - 콜백 함수의 반환 값이 참이면 해당 요소를 반환

- some

    - 배열의 요소 중 적어도 하나라도 콜백 함수를 통과하면 true를 반환하며 즉시 배열 순회 중지

    - 반면에 모두 통과하지 못하면 false를 반환

- every

    - 배열의 모든 요소가 콜백 함수를 통과하면 true를 반환

    - 반면에 하나라도 통과하지 못하면 즉시 false를 반환하고 배열 순회 중지

<br>

### 콜백함수 구조 사용 이유

- 함수의 재사용성 측면

    - 함수를 호출하는 코드에서 콜백 함수의 동작을 자유롭게 변경할 수 있음

- 비동기적 처리 측면