FROM python:3.11-slim

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    build-essential \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
