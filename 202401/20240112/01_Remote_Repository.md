# Remote Repository

<br>

### 원격 저장소

- 코드와 버전 관리 이력의 온라인 상의 특정 위치에 저장하여 여러 개발자가 협업하고 코드를 공유할 수 있는 공간

<br>

### add commit push 정의

- add : 로컬에서 스테이지에 변경사항을 추가한다.

- commit : 스테이지 변경사항에 메모를 남긴다.

- push : 스테이지에 있는 내용을 원격저장소에 보낸다.

<br>

### 추가

- git reset : add 취소

- git commit --amend : commit 메세지 변경

- git remote add (저장소이름) (저장소주소) : 이름으로 원격저장소 주소를 추가

- git push --set-upstream (저장소이름) (브랜치) : 저장소에 푸쉬할 때 해당 브랜치를 기본 브랜치로 설정

- git remote -v : 원격저장소의 이름 목록 확인

- git push -u (저장소이름) (브랜치) : 저장소에 브랜치 푸쉬

- git pull (저장소이름) (브랜치) : 원격저장소의 브랜치에서 변경사항 가져오기

- git clone (저장소주소) : 원격저장소 전체를 복제