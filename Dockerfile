FROM python:3.6

RUN mkdir /code
WORKDIR /code
COPY . .

RUN pip install pipenv
RUN pipenv install

EXPOSE 8000

CMD['sh', 'start.sh']