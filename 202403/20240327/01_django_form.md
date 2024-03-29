# django form

<br>

### HTML Form

- 사용자로부터 데이터를 받기 위해 활용한 방법

- 비정상적 혹은 악의적인 요청을 필터링 할 수 없음

- 유효한 데이터인지에 대한 확인이 필요

<br>

### 유효성 검사

- 수집한 데이터가 정확하고 유효한지 확인하는 과정

- 입력 값, 형식, 중복, 보안 등 많은 것들을 고려해야 함

- 이를 위해 Django가 제공하는 Form을 사용

<br>

### Django Form

- 사용자 입력 데이터를 수집하고 처리 및 유효성 검사를 수행하기 위한 도구

- 유효성 검사를 단순화하고 자동화 할 수 있는 기회를 제공

- Forms.py 생성 후 Form class 정의

- Form rendering options : label, input 쌍을 특정 HTML 태그로 감싸는 옵션

<br>

### Widgets

- HTML 'input' element의 표현을 담당

- Widget은 단순히 input 요소의 속성 및 출력되는 부분을 변경하는 것

<br>

### ModelForm

- Form : 사용자 입력 데이터를 DB에 저장하지 않을 때

- ModelForm : 사용자 입력 데이터를 DB에 저장해야 할 때

- Model과 연결된 Form을 자동으로 생성해주는 기능을 제공

<br>

### Meta class

- ModelFrom의 정보를 작성하는 곳

- fields : 모델에서 사용할 필드를 지정

- exclude : 포함하지 않을 필드를 지정

<br>

### is_valid()

- 여러 유효성 데이터를 실행하고 데이터가 유효한지 여부를  Boolean으로 반환

- 별도로 명시하지 않았지만 모델 필드에는 기본적으로 빈값은 허용하지 않는 제약조건이 설정되어 있음

- 빈 값은 is_valid()에 의해 False로 평가되고 form 객체에는 그에 맞는 에러 메시지가 포함되어 다음 코드로 진행됨

<br>

### save()

- 데이터베이스 객체를 만들고 저장

- 생성과 수정을 구분하는 법 : instance 여부를 통해 생성과 수정을 결정

<br>

### Django Form 정리

- 사용자로부터 데이터를 수집하고 처리하기 위한 강력하고 유연한 도구

- HTML Form의 생성, 데이터 유효성 검사 및 처리를 쉽게 할 수 있도록 도움

<br>

### view 함수 구조 변화

- 동일한 목적을 가지는 두개의 view 함수를 하나로 구조화

- HTTP request method 차이점을 활용해 GET요청과 POST요청 처리를 한 함수에 구현