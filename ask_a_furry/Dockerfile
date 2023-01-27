FROM python:latest

RUN pip install gunicorn Django psycopg2
WORKDIR /usr/src/app
COPY . .
RUN ls -la
CMD ["gunicorn", "ask_a_furry.wsgi:application", "--bind", "0.0.0.0:8000"]

