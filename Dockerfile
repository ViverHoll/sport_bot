FROM python:3.11.9-alpine

ENV PYTHONUNBUFFERED = 1

WORKDIR /my_app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "-m", "app"]

