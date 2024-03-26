# ORM

<br>

### ORM(Object-Relational-Mapping)

- 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간에 데이터를 변환하는 기술

- 서로 다른 언어를 사용하는 시스템 간 통역 역할

<br>

### QuerySet API

- ORM에서 데이터를 검색, 필터링 정렬 및 그룹화 하는데 사용하는 도구

- API를 사용하여 SQL이 아닌 Python 코드로 데이터를 처리

- Article.objects.all()

<br>

### Query

- 데이터베이스에서 특정한 데이터를 보여 달라는 요청

- 원하는 데이터를 얻기 위해 데이터 베이스에 요청을 보낼 코드(쿼리문)를 작성

- 파이썬 코드가 ORM을 통해 SQL로 변환되어 DB로 전달, 응답데이터를 ORM이 QuerySet이라는 자료형태로 변환하여 우리에게 전달

<br>

### QuerySet

- 데이터베이스에게서 전달 받은 객체 목록(데이터 모음, 순회 가능)

- Django ORM을 통해 만들어진 자료형

- 단, 데이터베이스가 단일한 객체를 반환할 때는 QuerySet이 아닌 모델(class)의 인스턴스로 반환됨

- QuerySet API는 python의 모델 클래스와 인스턴스를 활용해 DB에 데이터를 저장, 조회, 수정, 삭제하는 것

<br>

### Django shell

- Django 환경 안에서 실행되는 python shell

- 입력하는 QuerySet API 구문이 Django 프로젝트에 영향을 미침

- django-extensions 설치 및 설정에 등록 후 python manage.py shell_plus


### QuerySet API 실습

- Create

    - 특정 테이블에 새로운 행을 추가하여 데이터 추가

        - 인스턴스 생성 후 인스턴스 변수에 값을 할당

    - QuerySet API 중 create() 메서드 활용

    - save() : 객체를 데이터 베이스에 저장하는 메서드

- Read

    - all() : 전체 데이터 조회

    - filter() : 특정 조건 데이터 조회
    
    - get() : 단일 데이터 조회

        - 객체를 찾을 수 없으면 DoesNotExist 예외를 발생시키고, 둘 이상의 객체를 찾으면 MultipleObjectsReturned 예외를 발생시킴

        - 위와 같은 특징을 가지고 있기 때문에 primary key와 같이 고유성(uniqueness)을 보장하는 조회에서 사용해야 함

- Update

    - 인스턴스 변경 후 save 메서드 호출

- Delete

    - 삭제하려는 데이터 조회 후 delete 메서드 호출

<br>

### Field lookups

- 특정 레코드에 대한 조건을 설정하는 방법

- QuerySet 메서드 filter(), exclude() 및 get()에 대한 키워드 인자로 지정

<br>

### ORM, QuerySet 사용이유

- 데이터베이스 쿼리를 추상화하여 Django 개발자가 데이터베이스와 직접 상호작용하지 않아도 되도록 함

- 데이터베이스와의 결합도를 낮추고 개발자가 더욱 직관적이고 생산적으로 개발할 수 있도록 도움