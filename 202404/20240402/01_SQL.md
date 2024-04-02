# SQL

<br>

### Database

- 데이터베이스 : 체계적인 데이터 모음

- 데이터 : 저장이나 처리에 효율적인 형태로 변환된 정보

- 데이터를 저장하고 조작(CRUD)

<br>

### 기존의 데이터 저장방식

- 파일을 이용한 데이터 관리

    - 어디서나 쉽게 이용가능

    - 구조적으로 관리하기 어려움

- 스프레드 시트를 이용한 데이터 관리

    - 테이블의 열과 행을 이용해 구조적으로 관리 가능

    - 일반적으로 약 100만 행까지만 저장 가능

    - 단순히 파일이나 링크 소유 여부에 따른 단순한 접근 권한 기능 제공

    - 데이터가 여러 시트에 분산되어 있다면 누락 또는 추가 문제가 발생할 수 있음

<br>

### 관계형 데이터베이스

- 관계 : 여러 테이블 간의 (논리적) 연결

- 데이터 간에 관계가 있는 데이터 항목들의 모음

- 테이블, 행, 열의 정보를 구조화하는 방식

- 서로 관련된 데이터 포인터를 저장하고 이에 대한 엑세스를 제공

<br>

### 관계형 데이터베이스 관련 키워드

- Table : 데이터를 기록하는 곳

- Field : Column, 각 필드에는 고유한 데이터 타입이 지정됨

- Record : Row, 각 레코드에는 구체적인 데이터 값이 저장됨

- Database : 테이블의 집합

- Primary Key(PK) : 각 레코드의 고유한 값, 레코드의 식별자로 사용

- Foreign Key(FK) : 외래 키, 테이블의 필드 중 다른 테이블의 레코드를 식별할 수 있는 키, 다른 테이블의 기본키를 참조, 서로 다른 테이블 간 관계를 만드는 데 사용

<br>

### DBMS

- 데이터베이스를 관리하는 소프트웨어 프로그램

- 데이터 저장 및 관리를 용이하게 하는 시스템

- 데이터베이스와 사용자 간의 인터페이스 역할

- 사용자가 데이터 구성, 업데이트, 모니터링, 백업, 복구 등을 할 수 있도록 도움

<br>

### RDBMS

- 관계형 데이터베이스를 관리하는 소프트웨어 프로그램

- SQLite, MySQL, Oracle Database 등

<br>

### 데이터베이스 정리

- Table은 데이터가 기록되는 곳

- Table에는 행에서 고유하게 식별 가능한 기본 키라는 속성이 있으며, 외래 키를 사용하여 각 행에서 서로 다른 테이블 간의 관계를 만들 수 있음

- 데이터는 기본 키 또는 외래 키를 통해 결합될 수 있는 여러 테이블에 걸쳐 구조화됨

<br>

### SQL

- 데이터베이스에 정보를 저장하고 처리하기 위한 프로그래밍 언어

- SQL Syntax

    - SQL 키워드는 대소문자를 구분하지 않음(명시적 구분을 위해 대문자로 작성 권장)

    - 각 SQL Statements의 끝에는 세미콜론(';')이 필요

<br>

### SQL Statements

- SQL을 구성하는 가장 기본적인 코드 블록

- 수행 목적에 따른 SQL Statements 4가지 유형

    - DDL : 데이터 정의 
        
        - 데이터의 기본 구조 및 형식 변경

        - CREATE, DROP, ALTER

    - DQL : 데이터 검색 
        
        - 데이터 검색

        - SELECT

    - DML : 데이터 조작 
        
        - 데이터 조작

        - INSERT, UPDATE, DELETE

    - DCL : 데이터 제어 
        
        - 데이터 및 작업에 대한 사용자 권한 제어

        - COMMIT, ROLLBACK, GRANT, REVOKE

<br>

### Query

- 데이터베이스로부터 정보를 요청

- 일반적으로 SQL로 작성하는 코드를 쿼리문(SQL문)이라 함

<br>

### SELECT

- 테이블에서 데이터를 조회 및 반환

- SELECT : 데이터를 선택하려는 필드를 하나 이상 지정

- FROM : 데이터를 선택하려는 테이블의 이름을 지정

<br>

### Sorting data

- ORDER BY : 조회 결과의 레코드를 정렬

    - ASC : 오름차순, 기본값

    - DESC : 내림차순

    - NULL 값이 존재할 경우 오름차순 정렬 시 결과에 NULL이 먼저 출력

<br>

### SELECT statement 실행 순서

1. FROM : 테이블에서

2. SELECT : 조회하여

3. ORDER BY : 정렬

<br>

### Filtering data 관련 키워드

- Clause

    - DISTINCT

    - WHERE

    - LIMIT

- Operator

    - BETWEEN

    - IN

    - LIKE

    - Comparision

    - Logical

<br>

### DISTINCT

- 조회 결과에서 중복된 레코드를 제거

- SELECT 바로 뒤에 작성

- 고유한 값을 선택하려는 하나 이상의 필드를 지정

<br>

### WHERE

- 조회 시 특정 검색 조건을 지정

- FROM clause 뒤에 위치

- search_condition은 비교연산자 및 논리연산자를 사용하는 구문이 사용

<br>

### Operators

- Comparision Operators : 비교 연산자

    - =, >=, <=, !=, IS, LIKE, IN, BETWEEN, ...

- Logical Operators : 논리 연산자

    - AND(&&), OR(||), not(!)

- IN Operators : 값이 특정 목록 안에 있는지 확인

- LIKE Operators : 값이 특정 패턴에 일치하는지 확인

    - Wildcard Characters

        - '%' : 0개 이상의 문자열과 일치하는지 확인

        - '_' : 단일문자와 일치하는지 확인

<br>

### LIMIT

- 조회하는 레코드 수를 제한

- 하나 또는 두개의 인자를 사용(0 또는 양의 정수)

- 조회하는 최대 레코드 수를 지정

<br>

### GROUP BY

- 레코드를 그룹화하여 요약본 생성(집계 함수와 함께 사용)

- Aggregation Functions(집계함수) : 값에 대한 계산을 수행하고 단일한 값을 반환하는 함수

    - SUM, AVG, MAX, MIN, COUNT

- FROM 및 WHERE 절 뒤에 배치

- 그룹화 할 필드 목록을 작성

<br>

### SELECT statement 실행 순서

1. FROM : 테이블에서

2. WHERE : 특정 조건에 맞추어

3. GROUP BY : 그룹화 하고

4. HAVING : 만약 그룹화 조건이 있다면 맞추고

5. SELECT : 조회하여

6. ORDER BY : 정렬

7. LIMIT : 특정 위치의 값을 가져옴

<br>

### CREATE TABLE

```
CREATE TABLE table_name (
    column_name data_type constraints,
    column_name data_type constraints,
)
```

- 테이블 생성

- 각 필드에 적용할 데이터 타입 작성

- 테이블 필드에 대한 제약조건 작성

<br>

### SQLite 데이터 타입

- NULL : 아무런 값을 포함하지 않음을 나타냄

- INTEGER : 정수

- REAL : 부동소수점

- TEXT : 문자열

- BLOB : 이미지, 동영상, 문서 등의 바이너리 데이터

<br>

### Constraints(제약조건)

- 테이블의 필드에 적용되는 규칙 또는 제한 사항

- 데이터의 무결성을 유지하고 데이터베이스의 일관성을 보장

- 대표 제약 조건

    - PRIMARY KEY : 해당 필드를 기본 키로 지정

    - NOT NULL : 해당 필드에 NULL 값을 허용하지 않도록 지정

    - FORIEIGN KEY : 다른 테이블과의 외래 키 관계를 정의

<br>

### AUTOINCREMENT

- 자동으로 정수 값을 생성하고 할당하는 필드 속성

- 필드의 자동 증가를 나타내는 특수 키워드

- 주로 primary key 필드에서 사용

- 삭제된 값은 무시되며 재사용할 수 없게 됨

<br>

### ALTER TABLE

- 테이블 및 필드 조작

- 역할

    - ADD COLUMN : 필드 추가

        - ADD COLUMN 후에 추가하고자 하는 새 필드 이름과 데이터 타입 및 제약 조건 작성
        
        - 단, 추가하고자 하는 필드에 NOT NULL 제약 조건이 있을 경우 NULL이 아닌 기본 값 설정 필요

        - SQLite는 단일 문을 사용하여 한번에 여러 필드를 추가할 수 없음

    - RENAME COLUMN : 필드 이름 변경

        - RENAME COLUMN 후에 이름을 바꾸려는 필드 지정 TO 후에 새 이름 지정
    
    - RENAME TO : 테이블 이름 변경

        - RENAME TO 후에 새 이름 지정

<br>

### DROP TABLE

- 테이블 삭제

- DROP TABLE 후에 삭제할 테이블 이름 지정

<br>

### 타입 선호도(Type Affinity)

- 컬럼에 데이터 타입이 명시적으로 지정되지 않았거나 지원하지 않을 때 SQLite가 자동으로 데이터 타입을 추론하는 것

- 목적

    - 유연한 데이터 타입 지원

    - 간편한 데이터 처리

    - SQL 호환성

<br>

### INSERT

```
INSERT INTO table_name (c1, c2, ...)
VALUES (v1, v2, ...);
```

- 테이블 레코드 삽입

- INSERT INTO 절 다음에 테이블 이름과 괄호 안에 필드 목록 작성

- VALUES 키워드 다음 괄호 안에 해당 필드에 삽입할 값 목록 작성

<br>

### UPDATE

```
UPDATE table_name
SET column_name = expression
[WHERE condition];
```

- 테이블 레코드 수정

- SET 절 다음에 수정 할 필드와 새 값을 지정

- WHERE 절에서 수정 할 레코드를 지정하는 조건 작성

- WHERE 절을 작성하지 않으면 모든 레코드를 수정

<br>

### DELETE

```
DELETE FROM table_name
[WHERE condition];
```

- 테이블 레코드 삭제

- DELETE FROM 절 다음에 테이블 이름 작성

- WHERE 절에서 삭제할 레코드를 지정하는 조건 작성

- WHERE 절을 작성하지 않으면 모든 레코드를 삭제

<br>

### JOIN

- 관계 : 여러 테이블 간의 (논리적) 연결

- 관계형 DB에서 필요한 순간에 잠깐 결합하여 출력

- 둘 이상의 테이블에서 데이터를 검색하는 방법

- 종류

    - INNER

    - LEFT

    - RIGHT

<br>

### INNER JOIN

```
SELECT selected_list
FROM table_a
INNER JOIN table_b
    ON table_b.fk = table_a.pk;
```

- 두 테이블에서 값이 일치하는 레코드에 대해서만 결과를 반환

- FROM 절 이후 메인 테이블 지정

- INNER JOIN 절 이후 메인 테이블과 조인할 테이블 지정

- ON 키워드 이후 조인 조건을 작성

- 조인 조건은 두 테이블 간의 레코드를 일치시키는 규칙을 지정

<br>

### LEFT JOIN

```
SELECT selected_list
FROM table_a
LEFT JOIN table_b
    ON table_b.fk = table_a.pk;
```

- 오른쪽 테이블의 일치하는 레코드와 함께 왼쪽 테이블의 모든 레코드 반환

- FROM 절 이후 왼쪽 테이블 지정

- LEFT JOIN 절 이후 오른쪽 테이블 지정

- ON 키워드 이후 조인 조건을 작성

- 왼쪽 테이블의 모든 레코드를 표시, 오른쪽 테이블과 매칭되는 레코드가 없으면 NULL을 표시