### CSS Box 모델

- 내용(content), 안쪽 여백(padding) 테두리(border) 외부 간격(margin)

- top, right, bottom, left 4방향

### 브라우저별 동일 CSS 적용법

- reset CSS : 브라우저의 모든 CSS 속성을 초기화

- normalize CSS : 일반적인 속성을 남김

### Box-sizing

- content-box

- border-box

### 박스타입(서술형)

- block

    - 줄바꿈 발생

    - 영역이 한 줄 차지

    - 높이, 너비 설정 가능

- inline

    - 줄바꿈이 발생하지 않음

    - 영역이 컨텐츠의 크기만큼 차지

    - 높이, 너비 설정 불가

- inline-block

    - 줄바꿈이 발생하지 않음

    - 영역이 컨텐츠의 크기만큼 차지

    - 높이, 너비 설정 가능

### Normal flow

- CSS를 적용하지 않았을 경우 웹페이지 요소가 기본적으로 배치되는 방향

### 속성에 따른 수평정렬

- block : 'margin: 0px auto;'

- inline : 부모 요소에 'text-align center'

### display:none;

- 공간을 차지하지 않음(visibility:hidden;과의 차이점)

### shorthand, 단축표현

- border

    - 순서 무관

    - border-width : 기본값 1px

    - border-style : 기본값 none

    - border-color : 기본값 검정색

- margin, padding

- 공통

- 상하/좌우

- 상/좌우/하

- 상/우/하/좌

### Position

- static : 기본값

- relative : 원래 자신의 위치에서 상대적인 위치

- absolute : 가장 가까운 부모 요소 중 static이 아닌 부모요소를 기준으로 배치

- fixed : 화면에 고정

- sticky : 이동하다가 해당 위치에서 화면에 고정