# /api-bridge/Dockerfile
FROM python:3.9.4-slim-buster

WORKDIR /app

COPY requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5001

CMD ["python", "app.py"]