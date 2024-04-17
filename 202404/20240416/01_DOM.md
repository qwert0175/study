# DOM

<br>

### 웹의 탄생(1990)

- Tim Berners-Lee 경이 WWW, 하이퍼텍스트 시스템 고안하여 개발

- URL, HTTP 최초 설계 및 구현

- 초기의 웹은 정적인 텍스트 페이지만을 지원

<br>

### 웹 브라우저의 대중화(1993)

- Netscape사의 최초 상용 웹 브라우저인 Netscape Navigator 출시

- 당시 약 90% 이상의 시장 점유율

- Netscape사는 웹의 동적인 기능을 만들기 위한 프로젝트를 시작

<br>

### JavaScript의 탄생(1995)

- 당시 Netscape 소속 개발자 Brandon Eich는 웹의 동적 기능 개발이라는 회사의 요구사항을 넘어 스크립트 언어 Mocha를 개발

- 이후 LiveScript로 이름을 변경했으나 당시 가장 인기 있던 프로그래밍 언어인 Java의 명성에 기대보고자 JavaScript로 이름을 변경

- JavaScript는 Netscape Navigator 2.0에 탑재되어 웹 페이지에 동적 기능을 추가하는데 사용됨

<br>

### JavaScript 파편화(1996)

- 그런에 Microsoft가 자체 웹 브라우저인 인터넷 익스플로러(IE) 3.0에 JavaScript와 유사한 언어인 JScript를 도입

- 이 과정에서 많은 회사들이 독자적으로 JavaScript룰 변경하고 이를 자체 브라우저에 탑재

- JavaScript 파편화의 시작

<br>

### ECMAScript 출시(1997)

- JavaScript의 파편화를 막기 위해 Netscape사는 ECMA 재단에 웹 표준 제작을 요청

- ECMA에서 ECMAScript라는 표준 언어를 정의하고 발표

- 이때부터 JavaScript는 ECMAScript 표준에 기반을 두고 발전하기 시작

<br>

### ECMAScript

- ECMA International이 정의하고 있는 표준화된 스크립트 프로그래밍 언어 명세

- 스크립트 언어가 준수해야 하는 규칙, 세부사항 등을 제공

<br>

### ECMAScript와 JavaScript

- JavaScript는 ECMAScript 표준을 구현한 구체적인 프로그래밍 언어

- ECMAScript의 명세를 기반으로 하여 웹 브라우저나 Node.js와 같은 환경에서 실행됨

- ECMAScript는 JavaScript의 표준이며, JavaScript는 ECMAScript 표준을 따르는 구체적인 프로그래밍 언어

- ECMAScript는 언어의 핵심을 정의하고 JavaScript는 ECMAScript 표준을 따라 구현된 언어로 사용됨

<br>

### ECMAScript의 역사

- ECMAScript 5(ES5)에서 안정성과 생산성을 크게 높임(2009)

- ECMAScript 2015(ES6)에서 객체지향 프로그래밍 언어로써 많은 발전을 이루어 역사상 가장 중요한 버전으로 평가됨(2015)

<br>

### JavaScript의 현재

- 현재는 Chrome, Firefox, Safari, Microsoft Edge 등 다양한 웹 브라우저가 경쟁하고 있으며 모바일 등 시장이 다양화 되어있음

- 기존에 JavaScript는 브라우저에서만 웹페이지의 동적인 기능을 구현하는 데에만 사용되었음

- 이후 Node.js로 인해 브라우저에서 벗어나 서버 사이드 분야 뿐만 아니라 클라이언트 사이드 등 다양한 프레임워크와 라이브러리들이 개발되면서 웹 개발 분야에서는 필수적인 언어로 자리잡게 됨

<br>

### JavaScript 실행 환경

- HTML script 태그

- js 확장자 파일

- 브라우저 Console

<br>

### DOM(The Document Object Model)

- 웹페이지를 구조화된 객체로 제공하여 프로그래밍 언어가 페이지 구조에 접근할 수 있는 방법을 제공

- 문서 구조, 스타일, 내용 등을 변경할 수 있도록 함

- DOM에서 모든 요소, 속성, 텍스트는 하나의 객체

- 모두 document 객체의 하위 객체로 구성됨

<br>

### DOM API

- 다른 프로그래밍 언어가 웹 페이지에 접근 및 조작 할 수 있도록 페이지 요소들을 객체 형태로 제공하며 이에 따른 메서드 또한 제공

<br>

### DOM tree

- 브라우저는 HTML 문서를 해석하여 DOM tree라는 객체 트리로 구조화

- 객체 간 상속 구조가 존재

<br>

### DOM 선택

- DOM 조작 순서

    1. 조작하고자 하는 요소를 선택(또는 탐색)

    2. 선택된 요소의 콘텐츠 또는 속성을 조작

- 선택 메서드

    - document.querySelector()

        - 제공한 선택자와 일치하는 element 한 개 선택

        - 제공한 CSS selector를 만족하는 첫 번째 element 객체를 반환

        - 없다면 null 반환

    - document.querySelectorAll()

        - 제공한 선택자와 일치하는 여러 element를 선택

        - 제공한 CSS selector를 만족하는 NodeList를 반환

<br>

### DOM 조작

- 속성(attribute) 조작

    - 클래스 속성 조작

    - 일반 속성 조작

- HTML 콘텐츠 조작

- DOM 요소 조작

- 스타일 조작

<br>

### 속성(attribute) 조작

- 클래스 속성 조작

    - classList property : 요소의 클래스 목록을 DOMTokenList(유사 배열) 형태로 반환

    - classList 메서드

        - element.classList.add() : 지정된 클래스 값을 추가

        - element.classList.remove() : 지정된 클래스 값을 제거

        - element.classList.toggle() : 클래스가 존재한다면 제거하고 false를 반환(존재하지 않으면 추가하고 true를 반환)

- 일반 속성 조작

    - element.getAttribute() : 해당 요소에 지정된 값을 반환(조회)

    - element.setAttribute(name,value) : 지정된 요소의 속성 값을 설정, 속성이 이미 있으면 기존 값을 갱신

    - element.removeAttribute() : 요소에서 지정된 이름을 가진 속성 제거

<br>

### HTML 콘텐츠 조작

- textContent property : 요소의 텍스트 콘텐츠를 표현

<br>

### DOM 요소 조작

- document.createElement(tagName) : 작성한 tagName의 HTML 요소를 생성하여 반환

- Node.appendChild() : 한 Node를 특정 부모 Node의 자식 NodeList 중 마지막 자식으로 삽입, 추가된 Node 객체를 반환

- Node,removeChild() : DOM에서 자식 Node 제거, 제거된 Node를 반환

<br>

### 스타일 조작

- style property : 해당 요소의 모든 style 속성 목록을 포함하는 속성

<br>

### Node

- DOM의 기본 구성 단위

- DOM 트리의 각 부분은 Node라는 객체로 표현됨

<br>

### NodeList

- DOM 메서드를 사용해 선택한 Node의 목록

- 배열과 유사한 구조를 가짐

- Index로만 각 항목에 접근 가능

- JavaScript의 배열 메서드 사용가능

- querySelectorAll()에 의해 반환되는 NodeList는 DOM의 변경사항을 실시간으로 반영하지 않음

<br>

### Element

- Node의 하위 유형

- Element는 DOM 트리에서 HTML 요소를 나타내는 특별한 유형의 Node

- HTML 태그들이 Element 노드를 생성

- Node의 속성과 메서드를 모두 가지고 있으며 추가적으로 요소 특화된 기능을 가지고 있음

<br>

### Parsing

- 브라우저가 문자열을 해석하여 DOM Tree로 만드는 과정