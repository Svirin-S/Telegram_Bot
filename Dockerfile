FROM python:3.9

SHELL ["/bin/bash", "-c"]

RUN pip install --upgrade pip

RUN apt update

EXPOSE 8000

COPY . .

WORKDIR /apu_with_restrictions/

RUN pip3 install -r requirements.txt

CMD ["gunicorn", "-b", "0.0.0.0:8000", "apu_with_restrictions.wsgi:application"]
