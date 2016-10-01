FROM docker:1.12-rc

RUN apk add --update \
    python \
    python-dev \
    py-pip \
    build-base \
  && pip install virtualenv \
  && rm -rf /var/cache/apk/*

COPY ./requirements.txt /script/
RUN virtualenv /env && /env/bin/pip install -r /script/requirements.txt

COPY ./main.py /script
CMD ["/env/bin/python", "/script/main.py"]

WORKDIR /app
