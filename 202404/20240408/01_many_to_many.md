# Many to many relationships

<br>

### Many to many relationships

- 한 테이블의 0개 이상의 레코드가 다른 테이블의 0개 이상의 레코드와 관련된 경우 양쪽 모두에서 N:1 관계를 가짐

<br>

### ManyToManyField(to, **options)

- M:N 관계 설정 모델 필드

- django에서는 ManyToManyField로 중개모델을 자동으로 생성

- 어디에 넣느냐에 따라 참조/역참조가 결정

<br>

### through argument

- 중개 테이블에서 추가 데이터를 사용해 M:N 관계를 형성하려는 경우에 사용

<br>

### M:N 관계 주요 사항

- M:N 관계로 맺어진 두 테이블에는 물리적인 변화가 없음

- ManyToManyField는 M:N 관계를 맺는 두 모델 어디에 위치해도 상관 없음

    - 대신 필드 작성 위치에 따라 참조와 역참조 방향을 주의할 것

- N:1은 완전한 종속의 관계였지만 M:N은 종속적인 관계가 아니며 의사에게 진찰받는 환자 & 환자를 진찰하는 의사 이렇게 두가지 형태 모두 표현 가능

<br>

### ManyToManyField의 대표인자 3가지

- related_name

    - 역참조시 사용하는 manager name을 변경

- symmetrical

    - 관계 설정 시 대칭 유무 설정
    
    - ManyToManyField가 동일한 모델을 가리키는 정의에서만 사용
    
    - 기본값 True

    - True일 경우

        - source 모델의 인스턴스가 target 모델의 인스턴스를 참조하면 자동으로 target 모델 인스턴스도 source 모델 인스턴스를 자동으로 참조하도록 함(대칭)

- through

    - 사용하고자 하는 중개모델을 지정

    - 일반적으로 추가 데이터를 M:N 관계와 연결하려는 경우에 활용

<br>

### M:N에서의 대표 methods

- add() : 지정된 객체를 관련 객체 집합에 추가

- remove() : 관련 객체 집합에서 지정된 모델 객체를 제거