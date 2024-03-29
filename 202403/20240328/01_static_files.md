# Static files

<br>

### Static files

- 서버 측에서 변경되지 않고 고정적으로 제공되는 파일

- 이미지, JS, CSS 파일 등

<br>

### 웹 서버와 정적 파일

- 웹 서버의 기본동작은 특정 위치에 있는 자원을 요청 받아서 응답을 처리하고 제공하는 것

- 웹 서버는 요청 받은 URL로 서버에 존재하는 정적 자원을 제공함

- 정적 파일을 제공하기 위한 경로(URL)가 있어야 함

<br>

### Static files 제공하기

- 기본 경로 : app폴더/static/

    - Static_URL : 기본 경로 및 추가 경로에 위치한 정적 파일을 참고하기 위한 URL, 실제 파일이나 디렉토리가 아니며 URL로만 존재

- 추가 경로 : STATICFILES_DIR에 문자열 값으로 추가 경로 설정

    - STATICFILES_DIR : 정적 파일의 기본 경로 외에 추가적인 경로 목록을 정의하는 리스트

<br>

### Media Files

- 사용자가 웹에서 업로드하는 정적 파일(user-uploaded)

<br>

### ImageField()

- 이미지 업로드에 사용하는 모델 필드

- 이미지 객체가 저장되는 것이 아닌 이미지 파일의 경로가 문자열로 DB에 저장

<br>

### 미디어 파일 제공을 위한 사전 준비

- settings.py에 MEDIA_ROOT,MEDIA_URL 설정

- 작성한 MEDIA_ROOT와 MEDIA_URL에 대한 url 지정

- MEDIA_ROOT : 실제 미디어 파일들이 위치하는 디렉토리의 절대 경로

- MEDIA_URL : MEDIA_ROOT에서 제공되는 미디어 파일에 대한 주소를 생성

<br>

### 이미지 업로드

1. models.py에서 ImageField 생성(blank=True: 공백 포함)

2. migration 진행(ImageField 사용 시 Pillow 라이브러리 필요)

3. form 요소의 enctype 속성 추가

4. view 함수에서 업로드 파일에 대한 추가 코드 작성

5. 이미지 업로드 양식 확인

6. 이미지 업로드 결과 확인

<br>

### 업로드 이미지 수정

1. 수정 페이지 form 요소에 enctype 속성 추가

2. update view 함수에서 업로드 파일에 대한 추가 코드 작성

<br>

### upload_to

- ImageField의 update_to 인자를 사용해 미디어 파일 추가 경로 설정

- 기본 경로 설정

    ```
    image = models.ImageField(blank=True, upload_to='images/')
    ```

- 업로드 날짜로 경로 설정

    ```
    image = models.ImageField(blank=True, upload_to='%Y/%m/%d')
    ```

- 함수 형식으로 경로 설정

    ```
    def articles_images_path(instance, filename):
        return f'images/{instance.user.username}/{filename}

    image = models.ImageField(blank=True, upload_to=articles_images_path)
    ```