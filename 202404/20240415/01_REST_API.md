# REST API

<br>

### 읽기 전용 필드(read_only_fields)

- 데이터를 전송받은 시점에 유효성 검사에서 제외시키고 데이터 조회 시에는 출력하는 필드

<br>

### Nested relationships(역참조 매니저 활용)

- 모델 관계 상으로 참조하는 대상은 참조되는 대상에 포함되거나 중첩될 수 있음

- 이러한 중첩된 관계는 serializers를 필드로 사용하여 표현 가능

<br>

### source arguments

- 필드를 채우는데 사용할 속성의 이름

- 점 표기법을 사용하여 속성을 탐색할 수 있음

- 읽기 전용필드 지정 이슈

    - 특정 필드를 override 혹은 추가한 경우 read_only_fields는 동작하지 않음

    - 이런 경우 새로운 필드에 read_only 키워드 인자로 작성해야 함

<br>

### API 문서화

- OpenAPI Specification : RESTful API를 설명하고 시각화하는 표준화된 방법

- API에 대한 세부사항을 기술할 수 있는 공식 표준

<br>

### 설계 우선 접근 법

- OAS의 핵심 이점

- API를 먼저 설계하고 명세를 작성한 후 이를 기반으로 코드를 구현하는 방식

- API의 일관성을 유지하고 API 사용자는 더 쉽게 API를 이해하고 사용할 수 있음

- 또한, OAS를 사용하면 API가 어떻게 작동하는지를 시각적으로 보여주는 문서를 생성할 수 있으며, 이는 API를 이해하고 테스트하는데 매우 유용

- 이런 목적으로 사용되는 도구가 Swager-UI 또는 ReDoc

<br>

### Django shortcuts functions

- render()

- redirect()

- get_object_or_404()

    - 모델 manager objects에서 get()을 호출하지만 해당 객체가 없을 땐 기존 DoesNotExist 예외 대신 Http404를 raise 함

- get_list_or_404()

    - 모델 manager objects에서 filter()의 결과를 반환하고 해당 객체목록이 없을 땐 Http404를 raise 함