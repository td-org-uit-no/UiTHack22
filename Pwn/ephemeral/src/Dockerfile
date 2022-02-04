FROM ubuntu:20.04
LABEL Description="UiTHack22 Ephemeral"
EXPOSE 7070

ENV EPHEMERAL_PASSWORD="1138"
ENV EPHEMERAL_FLAG="UiTHack22{the-timing-oracle-of-delphi}"

# Installation
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y socat

# User
RUN adduser --disabled-password --gecos "" jedi

COPY ephemeral /home/jedi
RUN chmod 555 /home/jedi/ephemeral

USER jedi
WORKDIR /home/jedi

CMD socat TCP-LISTEN:7070,reuseaddr,fork EXEC:"/home/jedi/ephemeral",pty,stderr