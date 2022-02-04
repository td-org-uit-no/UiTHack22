FROM ubuntu:20.04
LABEL Description="UiTHack22 only-droids"

# RUN apt-get update && apt-get install -y curl
# RUN apt-get install build-essential -y

# ENV CARGO_MANIFEST_DIR=/code

WORKDIR /code

COPY only-droids-binary .
COPY only-droids/static ./static
COPY only-droids/templates ./templates

EXPOSE 7500

CMD ./only-droids-binary
