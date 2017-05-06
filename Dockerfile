FROM python:3
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

ENV GUNICORN_CMD_ARGS="--bind=0:8000 --worker-class=gthread --threads=10"
CMD ["gunicorn", "app:app"]