# Router

<br>

### Routing

- 네트워크에서 경로를 선택하는 프로세스

- 웹 애플리케이션에서 다른 페이지 간의 전환과 경로를 관리하는 기술

<br>

### SSR에서의 Routing

- SSR에서 routing은 서버 측에서 수행

- 서버가 사용자가 방문한 URL 경로를 기반으로 응답을 전송

- 링크를 클릭하면 브라우저는 서버로부터 HTML 응답을 수신하고 새 HTML로 전체 페이지를 다시 로드

<br>

### CSR에서의 Routing

- CSR에서 routing은 클라이언트 측에서 수행

- 클라이언트 측 JavaScript가 새 데이터를 동적으로 가져와 전체 페이지를 다시 로드 하지 않음

<br>

### SPA에서 Routing이 없다면

- 유저가 URL을 통한 페이지의 변화를 감지할 수 없음

- 페이지가 무엇을 렌더링 중인지에 대한 상태를 알 수 없음

    - URL이 1개이기 때문에 새로고침 시 처음 페이지로 되돌아감

    - 링크를 공유할 시 첫 페이지만 공유 가능

- 브라우저의 뒤로 가기 기능을 사용할 수 없음

- 페이지는 1개이지만 주소에 따라 여러 컴포넌트를 새로 렌더링하여 마치 여러개의 페이지를 사용하는 것처럼 보이도록 해야 함

<br>

### Vue Router

- Vue 공식 라우터

- Vite로 프로젝트 생성 시 Router 추가

<br>

### Vue 프로젝트 구조 변화

- App.vue 코드 변화

- router 폴더 신규 생성

- views 폴더 신규 생성

<br>

### RouterLink

- 페이지를 다시 로드하지 않고 URL을 변경하여 URL 생성 및 관련 로직을 처리

- HTML의 a 태그를 렌더링

<br>

### RouterView

- RouterLink URL에 해당하는 컴포넌트를 표시

- 원하는 곳에 배치하여 컴포넌트를 레이아웃에 표시할 수 있음

<br>

### router/index.js

- 라우팅에 관련된 정보 및 설정이 작성되는 곳

- router에 URL과 컴포넌트를 매핑

<br>

### view

- RouterView 위치에 렌더링 할 컴포넌트를 배치

- 기존 components 폴더와 기능적으로 다른 것은 없으며 단순 분류의 의미로 구성됨

- 일반 컴포넌트와 구분하기 위해 컴포넌트 이름을 vue로 끝나도록 작성하는 것을 권장

<br>

### Named Routes

- 경로에 이름을 지정하는 라우팅

- name 속성 값에 경로에 대한 이름을 지정

- 경로에 연결하려면 RouterLink에 v-bind를 사용해 'to' props 객체로 전달

- 하드 코딩된 URL을 사용하지 않아도 됨

- URL 입력 시 오타 방지

<br>

### Dynamic Route Matching

- URL의 일부를 변수로 사용하여 경로를 동적으로 매칭

- 매개 변수를 사용한 동적 경로 매칭

<br>

### Nested Routes

- 중첩된 라우팅

- 애플리케이션의 UI는 여러 레벨 깊이로 중첩된 컴포넌트로 구성되기도 함

- 이 경우 URL을 중첩된 컴포넌트의 구조에 따라 변경되도록 이 관계를 표현할 수 있음

- 컴포넌트 간 부모-자식 관점이 아닌 URL에서의 중첩된 관계를 표현하는 관점으로 바라보기

<br>

### Children 옵션

- 배열형태로 필요한 만큼 중첩 관계를 표현할 수 있음

<br>

### Programatic Navigation

- RouterLink 대신 JavaScript를 사용해 페이지를 이동하는 것

- 프로그래밍 방식 네비게이션

- router 메서드

    - 다른 위치로 이동하기 : router.push()

    - 현재 위치 바꾸기 : router.replace()

<br>

### router.push()

- 다른 URL로 이동하는 메서드

- 새 항목을 history stack에 push하므로 사용자가 브라우저 뒤로 가기 버튼을 클릭하면 이전 URL로 이동할 수 있음

- RouterLink를 클릭했을 때 내부적으로 호출되는 메서드이므로 RouterLink를 클릭하는 것은 router.push()를 호출하는 것과 같음

<br>

### router.replace()

- push 메서드와 달리 history stack에 새로운 항목을 push 하지 않고 다른 URL로 이동(=== 이동 전 URL로 뒤로 가기 불가)

<br>

### Navigation Guard

- Vue router를 통해 특정 URL에 접근할 때 다른 URL로 redirect를 하거나 취소하여 내비게이션을 보호

- 라우트 전환 전/후 자동으로 실행되는 Hook

<br>

### Navigation Guard 종류

- Globally(전역 가드) : 애플리케이션 전역에서 모든 라우트 전환에 적용되는 가드

- Per-route(라우터 가드) : 특정 라우트에만 적용되는 가드

- In-component(컴포넌트 가드) : 컴포넌트 내에서만 적용되는 가드

<br>

### Globally Guard

- 애플리케이션 전역에서 동작하는 가드

- index.js에 작성

- beforeEach()

    - 다른 URL로 이동하기 직전에 실행되는 함수

    - 모든 가드는 2개의 인자를 받음

        - to : 이동할 URL 정보가 담긴 Route 객체

        - from : 현재 URL 정보가 담긴 Route 객체

    - 선택적으로 다음 값 중 하나를 반환

        - false : 현재 내비게이션을 취소, 브라우저 URL이 변경될 경우 'from' 경로의 URL로 재설정

        - Route Location : router.push()를 호출하는 것처럼 경로 위치를 전달하여 다른 위치로 redirect, return이 없다면 자동으로 'to' URL Route 객체로 이동

- beforeResolve()

- afterEach()

<br>

### Per-route Guard

- 특정 라우터에서만 동작하는 가드

- index.js의 각 routes에 작성

- beforeEnter()

    - 특정 route에 진입했을 때만 실행되는 함수

    - 단순히 URL의 매개변수나 쿼리 값이 변경될 때는 실행되지 않고 다른 URL에서 탐색해 올 때만 실행됨

<br>

### In-component Guard

- 특정 컴포넌트에서만 작동하는 가드

- 각 컴포넌트의 script에 작성

- onBeforeRouteLeave()

    - 현재 라우트에서 다른 라우트로 이동하기 전에 실행

    - 사용자가 현재 페이지를 떠나는 동작에 대한 로직을 처리

- onBeforeRouteUpdate()

    - 이미 렌더링 된 컴포넌트가 같은 라우트 내에서 업데이트 되기 전에 실행

    - 라우트 업데이트 시 추가적인 로직을 처리

### Lazy Loading Routes

- Vue 애플리케이션 첫 빌드 시 해당 컴포넌트를 로드 하지 않고 해당 경로를 처음으로 방문할 때 컴포넌트를 로드하는 것

- 앱을 빌드할 때 처음부터 모든 컴포넌트를 준비하면 컴포넌트의 크기에 따라 페이지 로드 시간이 길어질 수 있기 때문