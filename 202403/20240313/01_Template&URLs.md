# Template & URLs

<br>

### Django Template system

- 데이터 표현을 제어하면서 표현과 관련된 부분을 담당

### Django Template language

- Template에서 조건, 반복, 변수 등의 프로그래밍적 기능을 제공하는 시스템

### DTL Syntax

1. Variable

    - render 함수의 세번째 인자로 딕셔너리 데이터를 사용

    - 딕셔너리 key에 해당하는 문자열이 template에서 사용가능한 변수명이 됨

    - dot('.')를 사용하여 변수 속성에 접근할 수 있음

2. Filters

    - 표시한 변수를 수정할 때 사용 (변수 + | 필터)

    - chained(연결)이 가능하며 일부 필터는 인자를 받기도 함

    - 약 60여개의 built-in template filters를 제공

3. Tags

    - 반복 또는 논리를 수행하여 제어 흐름을 만듦

    - 일부 태그는 시작과 종료 태그가 필요

    - 약 24개의 built-in template filters를 제공

4. Comments

    - DTL에서의 주석

<br>

### 템플릿 상속

- 기본 템플릿 구조의 한계

- 페이지의 공통요소를 포함하고, 하위 템플릿이 재정의 할 수 있는 공간을 정의하는 기본 'skeleton' 템플릿을 작성하여 상속 구조를 구축

- 'extends' tag

    ```
    {% extends 'path' %}
    ```

    - 자식(하위) 템플릿이 부모 템플릿을 확장한다는 것을 알림

    - 반드시 최상단에 작성, 2개 이상 사용 불가

- 'block' tag

    ```
    {% block name %}
    {% endblock name %}
    ```

    - 하위 템플릿에서 재정의 할 수 있는 블록을 정의

    - 상위 템플릿에 작성하며 하위 템플릿이 작성할 수 있는 공간을 지정하는 것

<br>

### HTML form(요청과 응답)

- 데이터를 보내고 가져오기

- HTML 'form' element를 통해 사용자와 애플리케이션 간의 상호작용

<br>

### 'form' element

- 사용자로부터 할당된 데이터를 서버로 전송

- 웹에서 사용자 정보를 입력하는 여러 방식(text, password, checkbox 등)을 제공

<br>

### 'action' & 'method'

- 데이터를 어디(action)로 어떤 방식(method)로 요청할지

- action

    - 입력 데이터가 전송될 URL을 지정(목적지)

    - 만약 이 속성을 지정하지 않으면 데이터는 현재 form이 있는 페이지의 URL로 보내짐

- method

    - 데이터를 어떤 방식으로 보낼 것인지 정의

    - 데이터의 HTTP request methods (GET, POST)를 지정

<br>

### 'input' element

- 사용자의 데이터를 입력 받을 수 있는 요소

<br>

### 'input' element

- 입력한 데이터에 붙이는 이름(key)

- 데이터를 제출했을 때 서버는 name 속성에 설정된 값을 통해서만 사용자가 입력한 데이터에 접근할 수 있음

<br>

### Query String Parameters

- 사용자의 입력 데이터를 URL 주소에 파라미터를 통해 서버로 보내는 방법

- 문자열은 앰퍼센드('&')로 연결된 key=value 쌍으로 구성되며, 기본 URL과는 물음표('?')로 구분됨

<br>

### HTTP request 객체

- form으로 전송한 데이터 뿐만 아니라 모든 요청 관련 데이터가 담겨 있음

- form 데이터를 가져오는 방법

    ```
    request.GET.get('key name')
    ```

<br>

### DTL 주의사항

- Python처럼 일부 프로그래밍 구조를 사용할 수 있지만 명칭을 그렇게 설계했을 뿐, Python 코드로 실행되는 것이 아니며 Python과는 관련 없음

- 프로그래밍적 로직이 아니라 표현을 위한 것임을 명시하기

- 프로그래밍적 로직은 되도록 view 함수에서 작성 및 처리할 것

- 공식 문서를 참고해 다양한 태그와 필터 사용해보기

<br>

### Variable Routing

- URL 일부에 변수를 포함시키는 것

    ```
    <path_converter:variable_name>
    ```

- Path converters : URL 변수의 타입을 지정(str, int 등 5가지 타입 지원)

<br>

### Trailing Slashes

- Django는 URL 끝에 '/'가 없다면 자동으로 붙임

- 기술적인 측면에서 '/' 여부에 따라 서로 다른 URL로 구분

- 그래서 Django는 검색 엔진이 혼동하지 않게 무조건 붙이는 것을 선택

- 모든 프레임워크가 이렇게 동작하는 것은 아니니 주의