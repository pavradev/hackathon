FROM docker:1.12-rc

RUN apk add --update \
    python \
    py-pip \
  && pip install virtualenv \
  && rm -rf /var/cache/apk/*

COPY . /script
RUN virtualenv /env && /env/bin/pip install -r /script/requirements.txt

CMD ["/env/bin/python", "/script/main.py"]

WORKDIR /app
