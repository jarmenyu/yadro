FROM python:3.9-alpine

RUN apk update && \
    apk add --no-cache bash wget

COPY 2.py text_for_2_task.txt /tmp/

WORKDIR /tmp

RUN chmod +x /tmp/2.py