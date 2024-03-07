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

### Position 유형별 특징

- static

    - 기본값, 요소를 Nomal Flow에 따라 배치

- relative

    - 요소를 Nomal Flow에 따라 배치

    - 자기 자신을 기준으로 이동

    - 요소가 차지하는 공간은 static일 때와 같음

- absolute

    - 요소를 Nomal Flow에서 제거

    - 가까운 relative 부모 요소를 기준으로 이동

    - 문서에서 요소가 차지하는 공간이 없어짐

- fixed

    - 요소를 Nomal Flow에서 제거

    - 현재 화면영역(viewport)을 기준으로 이동

    - 문서에서 요소가 차지하는 공간이 없어짐

- sticky

    - 요소를 Nomal Flow에 따라 배치

    - 요소가 일반적인 문서 흐름에 따라 배치되다가 스크롤이 특정 임계점에 도달하면 그 위치에서 고정됨(fixed)

    - 만약 다음 sticky 요소가 나오면 다음 sticky 요소가 이전 sticky 요소의 자리를 대체(이전 sticky 요소가 고정되어 있던 위치와 다음 sticky 요소가 고정되어야 할 위치가 겹치게 되기 때문)

<br>

### z-index

- 요소가 겹쳤을 때 어떤 요소 순으로 위에 나타낼지 결정

- 정수값을 사용해 Z축 순서를 지정

- 더 큰 값을 가진 요소가 작은 값의 요소를 덮음

<br>

### Position의 역할

- 전체 페이지에 대한 레이아웃을 조정하는 것이 아닌 페이지 특정 항목의 위치를 조정하는 것

<br>

### Flexbox

- 요소를 행과 열 형태로 배치하는 1차원 레이아웃 방식

- main axis(주 축)

    - flex item들이 배치되는 기본 축

    - main start에서 시작하여 main end 방향으로 배치(기본값)

- cross axis(교차 축)

    - main axis에서 수직인 축

    - cross start에서 시작하여 cross end 방향으로 배치(기본값)

- Flex Container

    - display: flex; 혹은 display: inline-flex;가 설정된 부모 요소

    - 이 컨테이너의 1차 자식 요소들이 Flex item이 됨

    - flexbox 속성 값들을 사용하여 자식 요소 Flex Item들을 배치하는 주체

- Flex Item

    - Flex Container 내부에 레이아웃 되는 항목

<br>

### 레이아웃 구성

- Flex Container 지정

    - Flex Item은 기본적으로 행으로 나열

    - Flex Item은 주 축의 시작선에서 시작

    - Flex Item은 교차 축의 크기를 채우기 위해 늘어남

- flex-direction

    - Flex Item이 나열되는 방향을 지정

    - column으로 지정할 경우 주 축이 변경됨

    - "-reverse"로 지정하면 flex item 배치의 시작 선과 끝선이 서로 바뀜

- flex-wrap

    - Flex Item 목록이 Flex Container의 한 행에 들어가지 않을 경우 다른 행에 배치할지 여부 설정

- justify-content

    - 주 축을 따라 Flex Item과 주위에 공간을 분배

- align-content

    - 교차 축을 따라 Flex Item과 주위에 공간을 분배

        - flex-wrap이 wrap 또는 wrap-reverse로 설정된 여러 행에만 적용

        - 한 줄 짜리 행에는 효과 없음

- align-items

    - 교차 축을 따라 flex item 행을 정렬

- align-self

    - 교차 축을 따라 개별 flex item을 정렬

- flow-grow

    - 남은 행 여백을 비율에 따라 각 flex item에 분배

        - 아이템이 컨테이너 내에서 확장하는 비율을 지정

- flow-basis

    - flex item의 초기 크기 값을 지정

    - flow-basis와 width 값을 동시에 적용한 경우 flow-basis가 우선

<br>

### Flexbox 설정

- Flex Container 관련 속성 : display, flex-direction, flex-wrap, justify-content, align-content, align-items

- Flex Item 관련 속성 : align-self, flex-grow, flex-basis, order

<br>

### 목적에 따른 속성 분류

- 배치 : flex-direction, flex-wrap

- 공간 분배 : justify-content, align-content

- 정렬 : align-items, align-self

<br>

### 속성명 팁

- justify : 주 축

- align : 교차 축

- content : 여러 줄

- items : 한 줄

- self : 요소 한개

<br>

### 반응형 레이아웃

- 다양한 디바이스와 화면 크기에 자동으로 적응하여 콘텐츠를 최적으로 표시하는 웹 레이아웃 방식