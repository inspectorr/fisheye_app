FROM node:8.16 as build-deps
WORKDIR /app/frontend
COPY frontend/ .
RUN yarn install
RUN yarn build

FROM python:3.9

RUN apt-get update

WORKDIR /app
COPY . .

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install -r requirements.txt

RUN chmod 777 start.sh

EXPOSE 8765

CMD ./start.sh
