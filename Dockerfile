FROM python:3.6-alpine

RUN apk update && apk add g++ python3-dev libffi-dev openssl-dev git
WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt 

COPY ./pethotel /app/

# CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000", 