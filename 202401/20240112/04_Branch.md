# Branch

<br>

### Branch

- 가지, 일종의 평행세계 같은 것

- branch를 만들면 원본과 똑같지만 별개의 공간이 생김

- 새로 만든 branch 수정 시 원본에 영향을 주지 않음

- 자유롭게 수정 후 원본과 합칠 수 있음

<br>

### 추가

- git branch : branch 목록

- git branch (branch 이름) : branch 생성

- git branch -d (branch 이름) : branch 삭제

- git checkout (branch 이름) : branch 체크아웃(전환)

<br>

### 되돌리기

- 이전 행동을 지우는 방법

  - 이전 행동이 다시 필요해지는 경우가 있을 수 있어 권장되지 않음

- 과거의 행동을 다시 가져오는 방법(revert)

  1. git log를 통해 해당 시점 로그 확인

  2. git revert (로그) : 해당 로그 시점으로 되돌림
