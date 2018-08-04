## askcompany

### 필요한 환경설정

dialogflow에서 Agent를 생성하고, 다음 설정값을 채워주세요. (윈도우는 지원하지 않습니다.)

```sh
# 경로: env.sh

export DIALOGFLOW_CLIENT_ACCESS_TOKEN="채워주세요"
export DIALOGFLOW_DEVELOPER_ACCESS_TOKEN="채워주세요"
export DIALOGFLOW_WEB_DEMO_URL="채워주세요"
```

다음 명령으로 필요한 라이브러리를 설치해주세요.

```sh
pip3 install -r requirements.txt
```

다음 명령으로 위 `env.sh` 환경변수를 로딩해주세요.

```sh
source env.sh
```

다음 명령으로 개발서버를 실행시킬 수 있습니다.

```sh
python3 manage.py runserver 0.0.0.0:80
```

다음 명령으로 "장고와 연동되는" Jupyter 서버를 실행시킬 수 있습니다.

```sh
python3 manage.py shell_plus --notebook
```

---

> 여러분의 파이썬/장고 페이스메이커가 되겠습니다.

+ https://fb.com/groups/askdjango
+ https://askcompany.kr
+ me@askcompany.kr

