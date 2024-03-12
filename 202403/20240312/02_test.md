### 프로젝트 생성 시 생성되는 파일들

- settings.py : 프로젝트의 모든 설정을 관리

- urls.py : 요청 들어오는 URL에 따라 이에 해당하는 적절한 views를 연결

- \_\_init__.py : 해당 폴더를 패키지로 인식하도록 설정하는 파일

- asgi.py : 비동기식 웹 서버와의 연결 관련 설정

- wsgi.py : 웹 서버와의 연결 관련 설정

- manage.py : Django 프로젝트와 다양한 방법으로 상호작용하는 커맨드라인 유틸리티

<br>

### 앱 생성 시 생성되는 파일들

- admin.py : 관리자용 페이지 설정

- models.py : DB와 관련된 Model을 정의

- views.py : HTTP 요청을 처리하고 해당 요청에 대한 응답을 반환

- apps.py : 앱의 정보가 작성된 곳

- tests.py : 프로젝트 테스트 코드를 작성하는 곳