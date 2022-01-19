FROM python:3.9-alpine

COPY . ./

#RUN apt-get update && apt-get install -y kafkacat

RUN apk add --no-cache cyrus-sasl cyrus-sasl-gssapiv2 krb5 openssl ca-certificates kcat
RUN apk add --no-cache curl python3 bash && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip

RUN pip3 install -e .

RUN if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache

USER 1001
HEALTHCHECK --interval=30s --timeout=10s CMD curl -s --fail http://localhost:${HEALTHCHECK_PORT}/health-check