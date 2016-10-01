FROM docker:1.12-rc

RUN apk add --update \
    python \
    py-pip \
  && pip install virtualenv \
  && rm -rf /var/cache/apk/*

RUN virtualenv /env

COPY ./main.py /script/
CMD ["/env/bin/python", "/script/main.py"]

WORKDIR /app