FROM python:3.6

ADD . /app
WORKDIR /app

RUN pip install -r requirements.txt
# RUN python manage.py migrate
# RUN python manage.py --noinput