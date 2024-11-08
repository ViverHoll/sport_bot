FROM python:3.12.7-alpine

ENV PYTHONPATH "${PYTHONPATH}:/app"
ENV PATH "/app/scripts:${PATH}"
ENV PYTHONUNBUFFERED = 1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ADD . /app/
RUN chmod +x /app/scripts/*
ENTRYPOINT ["docker-entrypoint.sh"]