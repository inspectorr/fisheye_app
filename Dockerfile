FROM python:3.9

RUN apt-get update

WORKDIR /app
COPY . .

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install -r requirements.txt

WORKDIR /app/frontend
RUN apt-get install -y git-core curl build-essential openssl libssl-dev \
 && git clone https://github.com/nodejs/node.git \
 && cd node \
 && ./configure \
 && make \
 && sudo make install
RUN npm install -g yarn
RUN yarn install && yarn build

WORKDIR /app
RUN chmod 777 start.sh

CMD ./start.sh
