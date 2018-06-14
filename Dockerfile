FROM python:3.6.2-slim

RUN mkdir /app

WORKDIR /app

ADD . .

RUN pip install -r requirement.txt

EXPOSE 5000

CMD ["python", "run.py", "runserver"]
