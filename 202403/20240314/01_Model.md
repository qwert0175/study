# Model

<br>

### App URL mapping

- 각 앱에 URL을 정의하는 것

- include() : 프로젝트 내부 앱들의 url을 참조할 수 있도록 매핑하는 함수

<br>

### Naming URL patterns

- URL에 이름을 지정하는 것

- path 함수의 name 인자를 정의해서 사용

- 'url' tag : 주어진 URL 패턴의 이름과 일치하는 절대 경로 주소를 반환

<br>

### URL 이름 공간

- 단순히 이름만으로 완벽하게 분리할 수 없음

- 이름에 key 사용

- {% url 'app_name:name' %}

<br>

### Django Model

- DB의 테이블을 정의하고 데이터를 조작할 수 있는 기능들을 제공

- 테이블 구조를 설계하는 청사진(blueprint)

- model 클래스 작성(id는 django가 자동으로 생성)

```
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
```

<br>

### Model class 살펴보기

- 클래스 변수명 : 테이블의 각 필드(열) 이름

- model Field 클래스 : 테이블 필드의 데이터 타입

- model Field 클래스의 키워드 인자(필드 옵션) : 테이블 필드의 제약조건 관련 설정

    - 제약조건 : 데이터가 올바르게 저장되고 관리되도록 하기 위한 규칙

<br>

### Migrations

- model 클래스의 변경사항(필드 생성, 수정, 삭제 등)을 DB에 최종 반영하는 방법

- Migrations 과정

    1. makemigrations

        ```
        python manage.py makemigrations
        ```

    2. migrate

        ```
        python manage.py migrate
        ```

<br>

### 추가 모델 필드 작성

- 필드를 나중에 추가하려면 필드의 기본값 필요

- makemigrations 시 새로운 migration 파일 생성(문제 발생시 복구에 용이)

- 'model class 변경 - makemigrations - migrate'가 일련의 과정

<br>

### Model Field

- db 테이블의 필드(열)을 정의하며 해당 필드에 저장되는 데이터 타입과 제약조건을 정의

- CharField : 길이의 제한이 있는 문자열을 넣을 때 사용

    - max_length : 필드의 최대길이, CharField의 필수 인자

- TextField : 글자 수가 많을 때 사용

- DateTimeField : 날짜와 시간을 넣을 때 사용

    - auto_now : 데이터가 저장될 때마다 자동으로 현재 날짜시간을 저장

    - auto_now_add : 데이터가 처음 생성될 때만 자동으로 현재 날짜시간을 저장

<br>

### Admin site

- Automatic admin interface

    - Django는 추가 설치 및 설정 없이 자동으로 관리자 인터페이스 제공

    - 데이터 확인 및 테스트 등을 진행하는데 매우 유용

1. admin 계정 생성

    - email은 선택사항이기 때문에 입력하지 않고 진행 가능

    - 비밀번호 입력 시 보안상 터미널에 출력되지 않으니 입력 이어가기

    ```
    python manage.py createsuperuser
    ```

2. DB에 생성된 admin 계정 확인

3. admin에 모델 클래스 등록

    ```
    from django.contrib import admin
    from .models import Article

    admin.site.register(Article)
    ```

4. admin site 로그인 후 등록된 모델 클래스 확인

5. 테이블 생성, 수정, 삭제 테스트

6. DB의 테이블 확인