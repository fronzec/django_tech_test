FROM python:3.8.0-alpine

RUN mkdir /code
WORKDIR /code
COPY . .

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install pipenv
RUN pipenv lock --requirements > requirements.txt
RUN pip install -r requirements.txt

ENTRYPOINT ["/code/start.sh"]
