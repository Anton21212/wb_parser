FROM python:3.10.7

WORKDIR /code

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .


EXPOSE 80

ENTRYPOINT ["/code/docker-entrypoint.sh"]
