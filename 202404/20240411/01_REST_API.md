# REST API

<br>

### API

- 두 소프트웨어가 서로 통신할 수 있게 하는 메커니즘

- 클라이언트-서버처럼 서로 다른 프로그램에서 요청과 응답을 받을 수 있도록 만든 체계

- 복잡한 코드를 추상화하여 대신 사용할 수 있는 몇 가지 더 쉬운 구문을 제공

<br>

### Web API

- 웹 서버 또는 웹 브라우저를 위한 API

- 현대 웹 개발은 하나부터 열까지 직접 개발하기보다 여러 Open API들을 활용하는 추세

<br>

### REST(Representational State Transfer)

- API server를 개발하기 위한 일종의 소프트웨어 방법론

- REST 원리를 따르는 시스템을 RESTful 하다고 부름

- 자원을 정의하고 자원에 대한 주소를 지정하는 전반적인 방법을 서술

<br>

### REST API

- REST라는 설계 디자인 약속을 지켜 구현한 API

<br>

### REST에서 자원을 사용하는 법 3가지

- 자원의 식별

    - URI

- 자원의 행위

    - HTTP Methods

- 자원의 표현

    - json 데이터

    - 궁극적으로 표현되는 데이터 결과물

### 자원의 식별

- URI : 인터넷에서 리소스(자원)를 식별하는 문자열

- URL : 웹에서 주어진 리소스의 주소

### URL 구조

- Schema

    - 브라우저가 리소스를 요청하는데 사용해야 하는 규약

    - URL의 첫 부분은 브라우저가 어떤 규약을 사용하는지를 나타냄

- Domain Name

    - 요청 중인 웹 서버를 나타냄

    - 어떤 웹 서버가 요구되는지를 가리키며 직접 IP 주소를 사용하는 것도 가능하지만, 사람이 외우기 어렵기 때문에 Domain Name으로 사용

- Port

    - 웹 서버의 리소스에 접근하는데 사용되는 기술적인 문

- Path

    - 웹 서버의 리소스 경로

    - 초기에는 실제 파일이 위치한 물리적인 위치를 나타냈지만 오늘날은 실제 위치가 아닌 추상화된 형태의 구조를 표현

- Parameters

    - 웹 서버에 제공하는 추가적인 데이터

    - '&' 기호로 구분되는 key-value 쌍 목록

    - 서버는 리소스를 응답하기 전에 이러한 파라미터를 사용하여 추가 작업을 수행 할 수 있음

- Anchor

    - 일종의 북마크를 나타내며 브라우저에 해당 지점에 있는 콘텐츠를 표시

    - fragment identifier(부분 식별자)라고 부르는 '#' 이후 부분은 서버에 전송되지 않음

<br>

### 자원의 행위

- HTTP Request Methods : 리소스에 대한 행위를 정의(HTTP verbs라고도 함)

<br>

### 대표 HTTP Request Methods

- GET : 서버에 리소스의 표현을 요청, GET을 사용하는 요청은 데이터만 검색해야 함

- POST : 데이터를 지정된 리소스에 제출, 서버의 상태를 변경

- PUT : 요청한 주소의 리소스를 수정

- DELETE : 지정된 리소스를 삭제

<br>

### HTTP response status codes

- 특정 HTTP 요청이 성공적으로 완료되었는지 여부를 나타냄

- Informational responses (100~199)

- Successful responses (200~299)

- Redirection responses (300~399)

- Client error responses (400~499)

- Server error responses (500~599)

<br>

### 자원의 표현

- 서버가 응답할 수 있는 것은 페이지 뿐만 아니라 다양한 데이터 타입을 응답할 수 있음

- REST API는 이 중에서도 JSON타입으로 응답하는 것을 권장

<br>

### DRF

- Django REST framework

- Django에서 Restful API 서버를 쉽게 구축할 수 있도록 도와주는 오픈소스 라이브러리

- 사전준비 Postman 설치

<br>

### Serialization(직렬화)

- 여러 시스템에서 활용하기 위해 데이터 구조나 객체 상태를 나중에 재구성할 수 있는 포맷으로 변환하는 과정

- 어떠한 언어나 환경에서도 나중에 다시 쉽게 사용할 수 있는 포맷으로 변환하는 과정

<br>

### Serializer

- Serialization을 진행하여 Serialized data를 반환해주는 클래스

<br>

### ModelSerializer

- Django 모델과 연결된 Serializer 클래스

- 일반 Serializer와 달리 사용자 입력 데이터를 받아 자동으로 모델 필드에 맞추어 Serialization을 진행

- many 옵션 : Serialize 대상이 QuerySet인 경우 입력

- data 속성 : Serialized data 객체에서 실제 데이터를 추출

<br>

### api_view decorator

- DRF view 함수에서는 필수로 작성되며 view 함수를 실행하기 전 HTTP 메서드를 확인

- 기본적으로 GET 메서드만 허용되며 다른 메서드 요청에 대해서는 405 Method Not Allowed로 응답

- DRF view 함수가 응답해야 하는 HTTP 메서드 목록을 작성

<br>

### partial argument

- 부분 업데이트를 허용하기 위한 인자

- False일 경우 수정하지 않은 다른 필드 데이터도 전송(유효성 검사)

<br>

### raise_exception

- is_valid()의 선택 인자

- 유효성 검사를 통과하지 못할 경우 ValidationError 예외를 발생시킴

- DRF에서 제공하는 기본 예외 처리기에 의해 자동으로 처리되며 기본적으로 HTTP 400 응답을 반환