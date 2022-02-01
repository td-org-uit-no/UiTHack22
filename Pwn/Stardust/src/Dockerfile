FROM ubuntu:20.04
LABEL Description="UiTHack22 stardust"
EXPOSE 8000

ENV MINDTRICK_FLAG="UiTHack22{The_Deathstar_Will_Be_Beutiful_but_Flawed}"

# Installation
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y socat
RUN apt-get install -y make gcc


# User
RUN adduser --disabled-password --gecos "" archivist

COPY stardust.c /home/archivist
COPY Makefile /home/archivist

WORKDIR /home/archivist
RUN make stardust
RUN chmod 555 /home/archivist/stardust

USER archivist

CMD socat TCP-LISTEN:8000,reuseaddr,fork EXEC:"/home/archivist/stardust",pty,stderr
