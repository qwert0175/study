# Django

<br>

### Web application 개발

- 인터넷을 통해 사용자에게 제공되는 소프트웨어 프로그램을 구축하는 과정

- 다양한 디바이스에서 웹 브라우저를 통해 접근하고 사용할 수 있음

<br>

### Client

- 서비스를 요청하는 주체

<br>

### Server

- 클라이언트의 요청에 응답하는 주체

<br>

### Frontend와 Backend

- Frontend : 사용자 인터페이스(UI)를 구성하고, 사용자가 애플리케이션과 상호작용할 수 있도록 함

- Backend : 서버 측에서 동작하며, 클라이언트의 요청에 대한 처리와 데이터베이스와의 상호작용을 담당

<br>

### Web Framework

- 웹 애플리케이션을 빠르게 개발할 수 있도록 도와주는 도구(개발에 필요한 기본 구조, 규칙, 라이브러리 등을 제공)

<br>

### Django

- Python 기반의 대표적인 웹 프레임워크

- Django를 사용하는 이유

    - 다양성 : Python 기반으로 소셜 미디어 및 빅데이터 관리 등 광범위한 서비스 개발에 적합

    - 확장성 : 대량의 데이터에 대해 빠르고 유연하게 확장할 수 있는 기능을 제공

    - 보안 : 취약점으로부터 보호하는 보안 기능이 기본적으로 내장되어 있음

    - 커뮤니티 지원 : 개발자를 위한 지원, 문서 및 업데이트를 제공하는 활성화 된 커뮤니티

- 검증된 웹 프레임워크(대규모 서비스에서도 안정적인 서비스 제공)

<br>

### 가상환경

- Python 애플리케이션과 그에 따른 패키지들을 격리하여 관리할 수 있는 독립적인 실행 환경

- 가상환경 사용 이유

    - 의존성 관리 : 라이브러리 및 패키지를 각 프로젝트마다 독립적으로 사용

    - 팀 프로젝트 협업 : 모든 팀원이 동일한 환경과 의존성 위에서 작업하여 버전간 충돌을 방지

- 가상환경 생성

    ```
    $ python -m venv venv
    ```

- 가상환경 활성화

    ```
    $ source venv/Scripts/activate
    ```

<br>

### 의존성 패키지

- 한 소프트웨어 패키지가 다른 패키지의 기능이나 코드를 사용하기 때문에 그 패키지가 존재해야만 제대로 작동하는 관계

- 사용하려는 패키지가 설치되지 않았거나 호환되는 버전이 아니면 오류가 발생하거나 예상치 못한 동작을 보일 수 있음

<br>

### 패키지 목록

- 가상환경에 대한 정보 공유

- 패키지 목록 텍스트파일 생성

    ```
    $ pip freeze > requirements.txt
    ```

- 패키지 목록 설치

    ```
    $ pip install -r requirements.txt
    ```

<br>

### Django 프로젝트 생성

1. 가상환경 생성

2. 가상환경 활성화

3. Django 설치

    ```
    $ pip install django
    ```

4. 의존성 파일 생성

5. .gitignore 파일 생성(첫 add 전)

6. git 저장소 생성

7. django 프로젝트 생성

    ```
    $ django-admin startproject firstpjt .
    ```

8. django 서버 실행

    ```
    python manage.py runserver
    ```

<br>

### 디자인 패턴

- 소프트웨어 설계에서 발생하는 문제를 해결하기 위한 일반적인 해결책

- 공통적인 문제를 해결하는 데 쓰이는 형식화된 관행

<br>

### MVC 디자인 패턴

- Model, View, Controller

- 애플리케이션을 구조화하는 대표적인 패턴

- 데이터, 사용자 인터페이스, 비즈니스 로직을 분리

<br>

### MTV 디자인 패턴

- Model, Template, View

- Django에서 애플리케이션을 구조화하는 패턴

- 기존 MVC 패턴과 동일하나 단순히 명칭을 다르게 정의한 것

<br>

### Project & App

- Project : 애플리케이션 집합

- Application : 독립적으로 작동하는 기능 단위 모듈

<br>

### 앱 생성 및 등록

1. 앱 생성

    ```
    $ python manage.py startapp articles
    ```

    - 앱 이름은 복수형 권장

2. 앱 등록

    - settings.py의 INSTALLED_APPS에 추가

<br>

### 프로젝트 구조

- settings.py : 프로젝트의 모든 설정을 관리

- urls.py : 요청 들어오는 URL에 따라 이에 해당하는 적절한 views를 연결

- \_\_init__.py : 해당 폴더를 패키지로 인식하도록 설정하는 파일

- asgi.py : 비동기식 웹 서버와의 연결 관련 설정

- wsgi.py : 웹 서버와의 연결 관련 설정

- manage.py : Django 프로젝트와 다양한 방법으로 상호작용하는 커맨드라인 유틸리티

<br>

### 앱 구조

- admin.py : 관리자용 페이지 설정

- models.py : DB와 관련된 Model을 정의

- views.py : HTTP 요청을 처리하고 해당 요청에 대한 응답을 반환

- apps.py : 앱의 정보가 작성된 곳

- tests.py : 프로젝트 테스트 코드를 작성하는 곳