# Bootstrap

<br>

### Bootstrap

- CSS 프론트엔드 프레임워크(Toolkit)

- 미리 만들어진 다양한 디자인 요소들을 제공하여 웹 사이트를 빠르고 쉽게 개발할 수 있도록 함

<br>

### CDN(Content Delivery Network)

- 지리적 제약 없이 빠르고 안전하게 콘텐츠를 전송할 수 있는 전송 기술

- 서버와 사용자 사이의 물리적인 거리를 줄여 콘텐츠 로딩에 소요되는 시간을 최소화 (웹 페이지 로드 속도를 높임)

- 지리적으로 사용자와 가까운 CDN 서버에 콘텐츠를 저장해서 사용자에게 전달

<br>

### Bootstrap 기본 사용법

- {property}{sides}-{size}

- property

    - m : margin

    - p : padding

- sides

    - t : top

    - b : bottom

    - s : left

    - e : right

    - y : top, bottom

    - x : left, right

    - blank : 4 sides

- size

    - 0 : 0rem, 0px

    - 1 : 0.25rem, 4px

    - 2 : 0.5rem, 8px

    - 3 : 1rem, 16px

    - 4 : 1.5rem, 24px

    - 5 : 3rem, 48px

    - auto : auto, auto

<br>

### reset CSS

- 모든 HTML 요소 스타일을 일관된 기준으로 재설정하는 간결하고 압축된 규칙 세트

- HTML Element, Table, List 등의 요소들에 일관성 있게 스타일을 적용시키는 기본 단계

- 브라우저마다 다른 User-agent stylesheets 설정을 초기화

- User-agent stylesheets : 모든 문서에 기본 스타일을 제공하는 기본 스타일 시트

<br>

### Normalize CSS

- Reset CSS 방법 중 대표적인 방법

- 웹 표준 기준으로 브라우저 중 하나가 불일치 한다면 차이가 있는 브라우저를 수정하는 방법

- Bootstrap은 bootstrap-reboot.css라는 파일명으로 normalize.css를 자체적으로 커스텀해서 사용하고 있음

<br>

### Typography

- 제목, 본문 텍스트, 목록 등

- Display headings : 기존 Heading보다 더 눈에 띄는 제목이 필요한 경우

- Inline text elements : HTML Inline 요소에 대한 스타일

- Lists : HTML list 요소에 대한 스타일

<br>

### Colors

- Bootstrap이 지정하고 제공하는 색상 시스템

- Text, Border, Background 및 다양한 요소에 사용하는 Bootstrap의 색상 키워드

<br>

### Bootstrap Component

- Bootstrap에서 제공하는 UI 관련 요소

- 일관된 디자인을 제공하여 웹 사이트의 구성 요소를 구축하는 데 유용하게 활용

<br>

### Bootstrap 사용 이유

- 가장 많이 사용되는 CSS 프레임워크

- 사전에 디자인된 다양한 컴포넌트 및 기능(빠른 개발과 유지보수)

- 손쉬운 반응형 웹 디자인 구현

- 커스터마이징이 용이

- 크로스 브라우징 지원(모든 주요 브라우저에서 작동되도록 설계)

<br>

### Semantic Web

- 웹 데이터를 의미론적으로 구조화된 형태로 표현하는 방식

<br>

### Semantic in HTML

- HTML 요소가 의미를 가진다는 것

- HTML Semantic Element : 기본적인 모양과 기능 이외에 의미를 가지는 HTML 요소

    - header, nav, main, article, section, aside, footer

<br>

### CSS 방법론

- CSS를 효율적이고 유지 보수가 용이하게 작성하기 위한 일련의 가이드라인

### OOCSS(Object Oriented CSS)

- 객체지향적 접근법을 적용하여 CSS를 구성하는 방법론

    1. 구조와 스킨을 분리

        - 재사용 가능성을 높임

        - 공통 구조를 정의 + 각각의 스킨을 정의

    2. 컨테이너와 콘텐츠를 분리

        - 객체에 직접 적용하는 대신 객체를 둘러싸는 컨테이너에 스타일을 적용

        - 스타일을 정의할 때 위치에 의존적인 스타일을 사용하지 않도록 함

        - 콘텐츠를 다른 컨테이너로 이동시키거나 재배치할 때 스타일이 깨지는 것을 방지

<br>

### 의미론적 마크업이 필요한 이유

- 검색엔진 최적화(SEO)

- 웹 접근성(Web Accessibility)