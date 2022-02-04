FROM ubuntu:20.04
LABEL Description="UiTHack22 Jedi Mind Trick"
EXPOSE 5600

ENV MINDTRICK_FLAG="UiTHack22{not-a-tale-the-jedi-would-tell-you}"

# Installation
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y socat

# User
RUN adduser --disabled-password --gecos "" jedi

COPY mindtrick /home/jedi
RUN chmod 555 /home/jedi/mindtrick

USER jedi
WORKDIR /home/jedi

CMD socat TCP-LISTEN:5600,reuseaddr,fork EXEC:"/home/jedi/mindtrick",pty,stderr