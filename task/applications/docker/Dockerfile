#Dockerfile
FROM python:3.8-alpine

WORKDIR /app

RUN pip install flask

COPY ./python-app/ .

EXPOSE 2024

CMD ["flask", "run", "--host", "0.0.0.0"]