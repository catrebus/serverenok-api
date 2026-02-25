FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ARG UID=1001
ARG GID=1001

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && \
    apt-get install -y lm-sensors && \
    rm -rf /var/lib/apt/lists/* && \
    python -m pip install --upgrade pip setuptools wheel && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

RUN groupadd -g $GID apiuser && useradd -m -u $UID -g $GID apiuser && \
    chown -R apiuser:apiuser /app
USER apiuser

CMD ["python", "main.py"]