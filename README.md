# .temp.python.fastapi
Python Basic Framework with FastAPI

## Prerequisite
- Python 3.7

## Feature
- dotenv(.env)를 이용한 config 구성
- SQLAlchemy ORM 구성
- SQLite를 기본 DB로 구성(./test.db)

## Porject Structure
```
└─app
    ├─api
    │  ├─v1
    │     ├─endpoints
    ├─core
    ├─crud
    ├─db
    ├─models
    ├─schemas
```
- **app.api.v1.endpoints** : Controller
- **app.core** : config, auth, security, etc
- **app.crud** : DAO
- **app.db** : DB setting
- **app.models** : ORM Model
- **app.schemas** : DTO

## Run
```
pip install pipenv
pipenv install
pipenv run uvicorn app.main:app --reload
```

## Swagger UI
- http://127.0.0.1:8000/docs
