# Many to one relationships

<br>

### Many to one relationships N:1 or 1:N

- 한 테이블의 0개 이상의 레코드가 다른 테이블의 레코드 1개와 관련된 관계

<br>

### ForeignKey()

- N:1 관계 설정 모델 필드

- ForeignKey 클래스의 인스턴스 이름은 참조하는 모델 클래스 이름의 단수형으로 작성하는 것을 권장

- 외래 키는 ForeignKey 클래스를 작성하는 위치와 관계없이 테이블 필드 마지막에 생성됨

- ForeignKey(to, on_delete)

    - to : 참조하는 모델 클래스 이름

    - on_delete : 외래 키가 참조하는 객체(1)가 사라졌을 때 외래 키를 가진 객체(N)를 어떻게 처리할 지를 정의하는 설정(데이터 무결성)

    - on_delete의 CASCADE : 부모객체가 삭제됐을 때 참조하는 객체도 삭제

<br>

### 역참조

- N:1 관계에서 1에서 N을 참조하거나 조회하는 것

- N은 외래 키를 가지고 있어 물리적으로 참조가 가능하지만 1은 N에 대한 참조 방법이 존재하지 않아 별도의 역참조 기능이 필요

- (모델 인스턴스).(역참조 모델)_set.(QuerySet API)

<br>

### related manager

- N:1 혹은 N:N 관계에서 역참조 시에 사용하는 매니저

- N:1 관계에서 생성되는 related manager의 이름은 참조하는 "모델명_set" 이름 규칙으로 만들어짐

<br>

### save(commit=False)

- DB에 저장하지 않고 인스턴스만 반환

<br>

### for empty 태그

- 내용이 없는 경우 작동

<br>

### 개수 출력하기

- DTL filter - 'length' 사용

```
{{comments|length}}

{{article.comment_set.all|length}}
```

- QuerySet API - 'count()' 사용

```
{{article.comment_set.count}}
```