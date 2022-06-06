FROM python:3.9

WORKDIR /bot

ADD bot_requirements.txt bot_requirements.txt
RUN pip install -r bot_requirements.txt

ADD bot.py bot.py
ADD .env .env

CMD python bot.py
