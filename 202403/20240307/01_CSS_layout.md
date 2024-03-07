# CSS layout

<br>

### CSS Box Model

- 모든 HTML 요소를 사각형 박스로 표현하는 개념

- 원은 네모 박스를 깎은 것

<br>

### Box 구성 요소

- Content : 내용, 콘텐츠가 표시되는 영역

- Padding : 안쪽, 콘텐츠 주위에 배치하는 공백 영역

- Border : 테두리, 콘텐츠와 패딩을 감싸는 테두리 영역

- Margin : 외부 간격, 이 박스와 다른 요소 사이의 공백, 가장 바깥쪽 영역

- top, left, right, bottom의 네 방향

- width & height 속성 : 요소의 너비와 높이를 지정

- 박스의 크기 : content 기준(box-sizing: content-box)이 기본값

<br>

### 박스 타입

- block : 좌상단에서 하단으로 배치

- inline : 좌상단에서 우측으로 배치

<br>

### Block 타입 특징

- 항상 새로운 행으로 나뉨

- width와 height 속성을 사용하여 너비와 높이를 지정할 수 있음

- 기본적으로 width 속성을 지정하지 않으면 박스는 inline 방향으로 사용가능한 공간을 모두 차지함

<br>

### Inline 타입 특징

- 새로운 행으로 나뉘지 않음

- width와 height 속성을 사용할 수 없음

- 수직방향

    - padding, margins, borders가 적용되지만 다른 요소를 밀어낼 수 없음

- 수평방향

    - padding, margins, borders가 적용되어 다른 요소를 밀어낼 수 있음

<br>

### Inline-block

- inline과 block 요소 사이의 중간 지점을 제공하는 display 값

- block 요소의 특징을 가짐

    - width, height 사용 가능

    - padding, margin 및 border로 인해 다른 요소가 밀려남

- 요소가 줄바꿈 되는걸 원하지 않으면서 너비와 높이를 적용하고 싶은 경우에 사용

<br>

### none

- 요소를 화면에 표시하지 않고 공간조차 부여되지 않음

<br>

### shorthand 속성 - border

- border-width, border-style, border-color를 한번에 설정하기 위한 속성

<br>

### shorthand 속성 - margin & padding

- 4방향의 속성을 각각 지정하지 않고 한번에 지정할 수 있는 속성

- 4개 : 상/우/하/좌

- 3개 : 상/좌우/하

- 2개 : 상하/좌우

- 1개 : 공통

<br>

### margin collapsing(마진 상쇄)

- 두 block 타입 요소의 margin top과 bottom이 만나 더 큰 margin으로 결합되는 현상

- 개발자가 레이아웃을 더욱 쉽게 관리할 수 있도록 함

- 각 요소에 대한 상/하 margin을 각각 설정하지 않고 한 요소에 대해서만 설정하기 위함

<br>

### CSS Layout

- 각 요소의 위치와 크기를 조정하여 웹 페이지의 디자인을 결정하는 것

- Display, Position, Float, Flexbox 등

<br>

### CSS Position

- 요소를 Normal Flow에서 제거하여 다른 위치로 배치하는 것

- 다른 요소 위에 올리기, 화면의 특정 위치에 고정시키기 등

- 유형 : static, relative, absolute, fixed, sticky

<br>