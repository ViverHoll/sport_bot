FROM python:3.12.7-alpine

ENV PYTHONPATH "${PYTHONPATH}:/app"
ENV PATH "/app/scripts:${PATH}"
ENV PYTHONUNBUFFERED = 1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
#RUN sudo apt-get update && sudo apt-get install -y make

COPY . .

#FROM ubuntu:24.04
#
##CMD ["python", "-m", "app"]
#
#RUN apt update && apt install -y make
#
#ENV PYTHONPATH "${PYTHONPATH}:/app"
#ENV PATH "/app/scripts:${PATH}"

ADD . /app/
RUN chmod +x /app/scripts/*
ENTRYPOINT ["docker-entrypoint.sh"]