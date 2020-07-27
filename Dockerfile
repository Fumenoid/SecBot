FROM python:3.7.8-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN apk add gcc python3-dev musl-dev

COPY bot.py .
COPY cogs .
COPY helpembed.py .
COPY requirements.txt .

RUN pip3 install -r requirements.txt
RUN pip3 install --upgrade discord.py

CMD ["python3", "bot.py"]
