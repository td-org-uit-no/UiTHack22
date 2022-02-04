FROM python:3.7-alpine
LABEL Description="UiTHack22 Leia"

WORKDIR /code
ENV FLASK_APP=server.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 7000

COPY . .
CMD ["flask", "run"]