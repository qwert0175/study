# Authentication System

<br>

### HTTP 특징

- 비 연결 지향 : 서버는 요청에 대한 응답을 보낸 후 연결을 끊음

- 무상태 : 연결을 끊는 순간 클라이언트와 서버 간의 통신이 끝나며 상태 정보가 유지되지 않음

- 상태를 유지하기 위한 기술이 필요

<br>

### 쿠키

- 서버가 사용자의 웹 브라우저에 전송하는 작은 전송조각

- 클라이언트 측에서 저장되는 작은 데이터 파일이며, 사용자 인증, 추적, 상태 유지 등에 사용되는 데이터 저장 방식

<br>

### 쿠키 사용 원리

1. 브라우저는 쿠키를 KEY-VALUE의 데이터 형식으로 저장

2. 동일한 서버에서 재요청 시 저장된 쿠키를 함께 전송

- 쿠키는 두 요청이 동일한 브라우저에서 들어왔는지 아닌지를 판단할 때 주로 사용됨

<br>

### 쿠키 사용 목적

- 세션 관리 : 로그인 아이디 자동완성, 공지 하루 안 보기, 팝업 체크, 장바구니 등의 정보 관리

- 개인화 : 사용자 선호, 테마 등의 설정

- 트래킹 : 사용자 행동을 기록 및 분석

<br>

### 세션

- 서버 측에서 생성되어 클라이언트와 서버 간의 상태를 유지

- 상태정보를 저장하는 데이터 저장 방식

- 쿠키에 세션 데이터를 저장하며 매 요청시마다 세션 데이터를 함께 보냄

### 세션 작동 원리

1. 클라이언트가 로그인을 하면 서버가 session 데이터를 생성 후 저장

2. session 데이터에 인증할 수 있는 session id 발급

3. 발급한 session id를 클라이언트에게 응답

4. 클라이언트는 응답 받은 session id를 쿠키에 저장

5. 클라이언트가 다시 동일한 서버에 접속하면 요청과 함께 쿠키(session id가 저장된)를 서버에 전달

6. 쿠키는 요청 때마다 서버에 함께 전송되므로 서버에서 session id를 확인해 로그인 되어있다는 것을 알도록 함

<br>

### Lifetime(수명)

- Session cookie

    - 현재 세션이 종료되면 삭제됨

    - 브라우저 종료와 함께 세션이 삭제됨

- Persistent cookies

    - Expires 속성에 지정된 날짜 혹은 Max-Age 속성에 지정된 기간이 지나면 삭제됨

<br>

### Django Authentication System(인증 시스템)

- auth 관련된 경로와 키워드들이 django 내부에서 accounts라는 이름으로 사용되기 때문에 accounts 사용을 권장

<br>

### Custom User Model 대체하기

- Django에서 기본적으로 제공하는 User Model이 아닌 직접 작성한 User Model 사용

- 기본적으로 제공된 User Model은 별도의 설정 없이 사용할 수 있어 간편하지만 직접 수정할 수 없는 문제가 존재

1. AbstractUser 클래스를 상속받는 커스텀 User 클래스 작성

    - 기존 User 클래스도 AbstractUser를 상속받기 때문에 커스텀 User 클래스도 기존 User 클래스와 같은 모습을 갖게 됨

2. settings.py에서 기본 User 모델을 작성된 User 모델로 지정

    - AUTH_USER_MODEL : Django 프로젝트의 User를 나타내는 데 사용하는 모델을 지정

    - 프로젝트 중간에 AUTH_USER_MODEL을 변경할 수 없음(처음에 변경)

3. admin site에 대체한 User 모델 등록

    - 기본 User 모델이 아니기 때문에 등록하지 않으면 출력되지 않음

<br>

### 주의사항

- Django는 새 프로젝트 시작 시 커스텀 User 모델을 설정하는 것을 강력하게 권장

- 커스텀 User 모델은 기본 User 모델과 동일하게 작동하면서도 필요한 경우 나중에 맞춤 설정할 수 있기 때문

- 단, 대체 작업은 프로젝트의 모든 migrations 혹은 첫 migrate 실행 전에 마쳐야 함

<br>

### Login

- Login : Session을 Create하는 과정

- AuthenticationForm() : 로그인 인증에 사용할 데이터를 입력 받는 built-in form

- login(request,user) : AuthenticationForm을 통해 인증된 사용자를 로그인 하는 함수

- get_user() : AuthenticationForm의 인스턴스 메서드, 사용자 객체를 반환

<br>

### Logout

- Logout : Session을 Delete하는 과정

- login(request) : 현재 요청에 대한 Session Data를 DB에서 삭제, 클라이언트의 쿠키에서도 Session Id를 삭제

<br>

### Template with Authentication data

- 템플릿에서 인증 관련 데이터를 출력하는 방법

<br>

### context processors

- 템플릿이 렌더링 될 때 호출 가능한 컨텍스트 목록

- 작성된 컨텍스트 데이터는 기본적으로 템플릿에서 사용가능한 변수로 포함됨

- django에서 자주 사용하는 데이터 목록을 미리 템플릿에 로드해둔 것

<br>

### AbstractUser class

- 관리자 권한과 함께 완전한 기능을 가지고 있는 User Model을 구현하는 추상 기본 클래스

<br>

### Abstract Base classes(추상 기본 클래스)

- 몇가지 공통 정보를 여러 다른 모델에 넣을 때 사용하는 클래스

- 데이터베이스 테이블을 만들 때 사용되지 않으며, 대신 다른 모델의 기본 클래스로 사용되는 경우 해당 필드가 하위 클래스의 필드에 추가됨