FROM python:3.9-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client \
    && apk add --update --no-cache --virtual .tmp-build-deps \ 
        gcc \
        libc-dev \
        linux-headers \
        postgresql-dev \
        musl-dev \
        zlib \
        zlib-dev \
    && pip install -r /requirements.txt \
    && apk del .tmp-build-deps \
    && mkdir /app
COPY ./app /app
WORKDIR /app
#CMD ["python", "/app/manage.py", "runserver", "0.0.0.0:8000"]