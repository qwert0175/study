# Many to one relationships

<br>

### User 모델을 참조하는 두가지 방법

- get_user_model()

    - 반환값 : User Object(객체)

    - 사용 위치 : models.py가 아닌 다른 모든 위치

- settings.AUTH_USER_MODEL

    - 반환값 : 'accounts.User'(문자열)

    - 사용 위치 : models.py

<br>

### require_POST

- 요청이 POST인지 확인하는 데코레이터

- 데코레이터 중첩 가능