# SamBank
SamBank é um projeto de uma API de um banco digital. Criei ele com o objetivo de obter aprendizado e experiência.

## Stack
- Frontend: React, VueJS (ainda não implementado)
- Backend: FastAPI
- DB: SQLAlchemy (SQLite3)
- Migrations: Alembic
- Tests: PyTest

# Como rodar
Clone: `https://github.com/pedroosamp/SamBank.git`

## Backend
2. Acesse o backend: `cd SamBank/backend`
3. Crie um venv: `python -m venv venv`
4. Ative o venv: `.\venv\Scripts\Activate.ps1`
5. Atualize o pip: `python -m pip install --upgrade pip`
6. Instale as dependencias: `pip install -r requirements.txt`
7. Aplique as migrations: `alembic upgrade head`
8. Rode as suites de teste: `pytest --disable-warnings -vv`
9. Rode o FastAPI: `uvicorn app.main:app --reload`
10. Acesse a documentação: `127.0.0.1:8000/docs`
