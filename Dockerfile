FROM python:3.13-slim

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml poetry.lock ./

RUN poetry install

COPY . .

EXPOSE 8001

CMD ["poetry", "run", "uvicorn", " src.main:app", "--host", "0.0.0.0", "--port", "8001"]