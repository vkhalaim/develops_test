FROM python:3.8

ENV PYTHONDONTWRITBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app

ADD news /app

CMD ["python", "manage.py", "runserver", "0.0.0.0", "8000"]