# HTML/CSS

<br>

### Web

- Web : Web site, Web application 등을 통해 사용자들이 정보를 검색하고 상호 작용하는 기술

- Web site : 인터넷에서 여러 개의 Web page가 모인 것으로 사용자들에게 정보나 서비스를 제공하는 공간

- Web page : HTML, CSS 등의 웹 기술을 이용하여 만들어진 Web site를 구성하는 하나의 요소

<br>

### HTML

- HTML : 웹 페이지의 의미와 구조를 정의하는 단어

- HyperText : 웹페이지를 다른 페이지로 연결하는 링크, 참조를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트

- Markup Language : 태그 등을 이용하여 데이터의 구조를 명시하는 언어

<br>

### HTML 구조

- DOCTYPE html : 해당 문서가 html 문서라는 것을 나타냄

- html 태그 : 전체 페이지의 콘텐츠를 포함

- title 태그 : 브라우저 탭 및 즐겨찾기 시 표시되는 제목으로 사용

- head 태그 : HTML 문서에 관련된 설명, 설정 등 사용자에게 보이지 않음

- body 태그 : 페이지에 표시되는 모든 콘텐츠

<br>

### HTML Element(요소)

- 하나의 요소는 여는 태그와 닫는 태그 그리고 그 안의 내용으로 구성됨

- 닫는 태그 이름 앞에 슬래시가 포함되며 닫는 태그가 없는 태그도 존재

<br>

### Text structure

- HTML의 주요 목적 중 하나는 텍스트 구조와 의미를 제공하는 것

- 대표적인 HTML Text structure

    - Heading & Paragraphs : h1~6, p

    - Lists : ol, ul, dl

    - Emphasis & Importance : em, strong

<br>

### CSS

- 웹 페이지의 디자인과 레이아웃을 구성하는 언어

- 선택자, 선언, 속성, 값

<br>

### CSS 적용

- 인라인 스타일 : HTML 요소 안에 style 속성 값으로 작성

- 내부 스타일 시트 : head 태그 안에 style 태그에 작성

- 외부 스타일 시트 : 별도의 CSS 파일 생성 후 HTML link 태그를 사용해 불러오기

<br>

### CSS Selectors

- HTML 요소를 선택하여 스타일을 적용할 수 있도록 하는 선택자

- 기본 선택자

    - 전체('*') 선택자 : 모든 HTML 요소를 선택

    - 요소(tag) 선택자 : 지정한 모든 태그를 선택

    - 클래스(class) 선택자 : 주어진 클래스 속성을 가진 모든 요소를 선택

    - 아이디(id) 선택자 : 주어진 고유한 아이디 속성을 가진 요소 선택

    - 속성(attr) 선택자

- 결합자

    - 자손 결합자(' '(space)) : 첫 번째 요소의 자손 요소들 선택

    - 자식 결합자('>') : 첫번째 요소의 직계 자식만 선택

<br>

### 명시도

- 결과적으로 요소에 적용할 CSS 선언을 결정하기 위한 알고리즘

- CSS Selector에 가중치를 계산하여 어떤 스타일을 적용할지 결정

- 동일한 요소를 가리키는 2개 이상의 CSS 규칙이 있는 경우 가장 높은 명시도를 가진 Selector가 승리하여 스타일이 적용됨

- 한 요소에 동일한 가중치를 가진 선택자가 적용될 때 CSS에서 마지막에 나오는 선언이 사용됨

<br>

### 상속

- 기본적으로 CSS는 상속을 통해 부모의 속성을 자식에게 상속하여 재사용성을 높임

- 상속되는 속성 : Text 관련 요소, opacity, visibility 등

- 상속되지 않는 속성 : Box model 관련 요소, position 관련 요소 등

<br>

### CSS 참고

- 인라인 스타일은 코드를 이해하기 어렵게 만드니 사용하지 말 것

- CSS는 외우지 않고 그때그때 검색하여 사용

- 속성은 되도록 class만 사용

