FROM python:3.9

WORKDIR /bot

ADD bot_requirements.txt bot_requirements.txt
RUN pip install -r bot_requirements.txt

ADD . .

CMD python bot.py
