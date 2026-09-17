FROM python:3.12-slim

WORKDIR /app

COPY app ./app
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "-c", "from app.scanner import check_password; print(check_password('Password123!'))"]
