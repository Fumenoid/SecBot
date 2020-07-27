FROM python:3.7.8-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN apk add gcc python3-dev musl-dev

COPY bot.py .
COPY cogs .
COPY helpembed.py .
COPY requirements.txt .
COPY configfile.py .

RUN pip install -r requirements.txt

CMD ["python", "bot.py"]