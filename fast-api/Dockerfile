FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

WORKDIR /app/app
COPY . /app/app

CMD ["uvicorn",  \
    "--host", "0.0.0.0", "--port", "80", \
    "--reload", \
    "app.main:app"]
