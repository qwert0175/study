# test

<br>

### requirements.txt에서 읽어와서 설치하는 명령어

- pip install -r requirements.txt

<br>

### 에러 이유 설명

- 예시

    - no such table : db에 테이블을 찾을 수 없음

    - 해결법 : makemigrations, migrate

    - makemigrations, migrate의 차이

<br>

### 최대 글자수 속성

- max_length

<br>

### form class 적용에서 4문제

- form 태그의 속성 action의 기능

- url 태그의 형태

- csrf 토큰

- django form을 변환

    - as_p

    - as_div
    
    - as_table

    - as_ul

<br>

### ModelForm class 정의

- 들어가서는 안되는 것 찾기

```
from django import forms
from .models import Article

class Article(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
```

<br>

### fields와 exclude 속성

- fields : 포함할 필드를 지정

- exclude : 포함하지 않을 필드를 지정

<br>

### 앱추가 시 등록

- srttings.py -> INSTALLED_APPS

<br>

### create와 update 차이점

- instance

<br>

### 생성 수정 삭제를 할 때 써야하는 메서드

- POST

<br>

### new, create 함수 결합 시 context 위치

- 들여쓰기 확인

<br>

### urls.py

- include() 2문제

- views.py의 에러 이유 1문제

<br>

### filter/all로 복수의 데이터를 가져왔을 때 반환되는 값의 type

- QuerySet

### 프로젝트/앱을 생성할 때 자동으로 어떤 옵션이 생기는지 생기지 않는지

### 

### DB에서 데이터 삭제하는 법

### urls.py를 보고 옳지 않은 것을 찾기

### admin 페이지

### MTV 디자인 패턴이 무엇인지 서술

### auto_now_add와 auto_now

### register