# Authentication

<br>

### 회원 가입

- User 객체를 Create 하는 과정

- UserCreateForm() : 회원 가입시 사용자 입력 데이터를 받는 built-in ModelForm

- 회원 가입 로직 작성 : UserCreationForm 사용

- 사용 시 주의사항 : UserCreationForm은 기존 유저 모델 사용, 커스텀 모델 사용시 설정 변경 필요(UserChangeForm도 함께 변경)

- 설정 변경 : forms.py 생성 후 class Meta: model = get_user_model()

    - get_user_model : 현재 프로젝트에서 활성화된 사용자 모델을 반환

<br>

### 회원 탈퇴

- User 객체를 Delete 하는 과정

- 이미 요청을 보낼 때 user 정보가 포함됨

- request.user.delete() 후 redirect

<br>

### 회원정보 수정

- User 객체를 Update 하는 과정

- UserChangeForm() : 회원정보 수정시 사용자 입력 데이터를 받는 built-in ModelForm

- 사용 시 주의 사항 : User 모델의 모든 정보들이 출력되어 수정이 가능하기 때문에 일반 사용자들이 접근해서는 안되는 정보는 차단 필요

- CustomChangeForm에서 접근 가능 필드를 설정

- instance 속성 사용

<br>

### 비밀번호 변경

- 인증된 사용자의 Session 데이터를 Update 하는 과정

- PasswordChangeForm() : 비밀번호 변경 시 사용자 입력 데이터를 받는 built-in Form

<br>

### 세션 무효화 방지하기

- 암호 변경 시 세션 무효화

    - 비밀번호가 변경되면 기존 세션과의 회원 인증 정보가 일치하지 않게 되어버려 로그인 상태가 유지되지 못하고 로그아웃 처리됨

    - 비밀번호가 변경되면서 기존 세션과의 회원 정보가 일치하지 않기 때문

- update_session_auth_hash(request,user) : 암호 변경 시 세션 무효화를 막아주는 함수(암호가 변경되면 새 암호로 기존 session을 자동으로 갱신)

<br>

### 인증된 사용자에 대한 접근 제한

- 로그인 사용자에 대해 접근을 제한하는 2가지 방법

    - is_authenticated 속성(attribute)

    - login_required 데코레이터(decorator)

- is_authenticated

    - 사용자가 인증되었는지 여부를 알 수 있는 User model의 속성

    - 모든 User 인스턴스에 대해 항상 True인 읽기 전용 속성이며, 비인증 사용자에 대해서는 항상 False

    - 로그인과 비로그인 상태의 화면 출력 설정 및 인증된 사용자의 로그인 및 회원가입 수행 차단

- login_required

    - 인증된 사용자에 대해서만 view 함수를 실행시키는 데코레이터

    - 비인증 사용자의 경우 로그인 주소로 redirect