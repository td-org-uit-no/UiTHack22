FROM ubuntu:20.04
LABEL Description="UiTHack22 stardust"
EXPOSE 5700

ENV FLAG="UiTHack22{The_Deathstar_Will_Be_Beutiful_but_Flawed}"

# Installation
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y socat
RUN apt-get install -y make gcc


# User
RUN adduser --disabled-password --gecos "" archivist

COPY stardust.c /home/archivist
COPY Makefile /home/archivist

WORKDIR /home/archivist
RUN make stardust
RUN rm stardust.c Makefile
RUN echo $FLAG > flag.txt
RUN chmod -R 555 /home/archivist

USER archivist
WORKDIR /home/archivist

CMD socat TCP-LISTEN:5700,reuseaddr,fork EXEC:"/home/archivist/stardust",pty,stderr