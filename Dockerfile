FROM python:3.12.7-alpine

ENV PYTHONUNBUFFERED = 1

WORKDIR /my_app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x scripts/*

CMD ["python", "-m", "app"]

