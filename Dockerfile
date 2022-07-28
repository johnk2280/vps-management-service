FROM python:3.10.4

RUN apt-get update &&  \
    apt-get install -y postgresql postgresql-contrib libpq-dev python3-dev

RUN pip3 install --upgrade pip

WORKDIR /app
COPY ./backend/vps_manager .
COPY ./requirements.txt .

RUN pip3 install -r requirements.txt
RUN python manage.py collectstatic --noinput
RUN ls -lia