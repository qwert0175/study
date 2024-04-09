# Many to many relationships

<br>

### .exists()

- QuerySet에 결과가 포함되어 있으면 True를 반환하고 결과가 포함되어 있지 않으면 False를 반환

- 큰 QuerySet에 있는 특정 객체 검색에 유용

<br>

### Fixtures

- Django가 데이터베이스로 가져오는 방법을 알고 있는 데이터 모음

- 데이터는 데이터베이스 구조에 맞추어 작성되어 있음

- 초기데이터 제공

<br>

### Fixtures 관련 명령어

- dumpdata : 생성(데이터 추출), 데이터베이스의 모든 데이터를 추출

- loaddata : 로드(데이터 입력), Fixtures 데이터를 데이터베이스로 불러오기

<br>

### Improve Query

- query 개선하기

- 같은 결과를 얻기 위해 DB 측에 보내는 query 개수 점차 줄여 조회하기

<br>

### annotate

- SQL의 GROUP BY를 사용

<br>

### select_related

- SQL의 INNER JOIN 사용

- 1:1 또는 N:1 참조 관계에서 사용

<br>

### prefetch_related

- SQL이 아닌 Python을 사용한 JOIN을 진행

- M:M 또는 N:1 역참조 관계에서 사용

