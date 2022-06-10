
# 개발환경 설정하기

### 1. 저장소 포크, 클론하기

Github에서 저장소를 포크하고, 로컬에 클론한다.

```bash
git clone https://github.com/<Username>/activity-time-tracking-system.git

cd activity-time-tracking-system
```

<br>

### 2. 파이썬 패키지 설치하기

[venv](https://docs.python.org/ko/3/library/venv.html)를 이용해 Python 가상 환경을 생성하고 필요한 패키지를 설치한다. 

```bash
python -m venv <가상환경 경로>

soruce <가상환경 경로>/bin/activate

pip install -r requirements.txt
```

> ⚠ 가상 환경을 생성하는 과정은 로컬 환경에 따라 달라질 수 있다.   

> ⚠ python 3.9 이상에서 backports.zoneinfo 설치 시 오류가 발생할 수 있다. 3.8 버전을 사용하면 문제가 발생하지 않는다.

<br>

### 3. settings.json 생성하기

activity-time-tracking-system/jamsinhs/settings.json 파일을 생성한다.

내용 예시:

```json
{
  "Production": false,
  "DEBUG": true,
  "SECRET_KEY": "django-insecure-*vseezuz7!()(-thm#-ot@dird!pl*e6a%+@umc0x@n=p3kfo&",
  "ALLOWED_HOSTS": ["127.0.0.1"]
}
```

SECRET_KEY는 Django에서 사용하는 값인데, 개발환경에서는 크게 중요하지 않다.   
예시에 사용된 값은 Django 프로젝트 생성 시 자동으로 설정된 값이다. 

<br>

### 4. 데이터베이스 초기화, 관리자 계정 생성하기

```bash
cd jamsinhs

python manage.py migrate

python manage.py createsuperuser
```

<br>

### 5. 개발 서버 실행, 테스트

코드 수정 후 개발 서버를 실행하거나 테스트를 통해 점검한다. 

```bash
cd jamsinhs

# 개발 서버 실행
python manage.py runserver

# 테스트
python manage.py test
```

<br>
