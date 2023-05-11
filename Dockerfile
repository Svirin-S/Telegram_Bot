FROM python:3.9

SHELL ["/bin/bash", "-c"]

RUN pip install --upgrade pip

RUN apt update

COPY . .

WORKDIR /Telegram_Bot/

RUN pip3 install -r requirements.txt

CMD ["python3", "main.py"]
