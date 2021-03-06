FROM python:3.9

RUN apt-get update

RUN curl https://deb.nodesource.com/setup_14.x | bash
RUN curl https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN apt-get install -y nodejs
RUN npm install -g yarn

WORKDIR /app
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app/frontend
ADD frontend/package.json package.json
ADD frontend/yarn.lock yarn.lock
RUN yarn install
ADD frontend .
RUN yarn build

WORKDIR /app

ADD . .

RUN chmod 777 start.sh

EXPOSE 8765

CMD ./start.sh
