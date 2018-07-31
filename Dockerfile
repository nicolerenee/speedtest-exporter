FROM debian:latest

RUN apt-get update && apt-get install -y \
  python-pip

RUN mkdir /app \
 && pip install speedtest-cli prometheus-client
COPY run-speedtest.py /app/

EXPOSE 9104
ENTRYPOINT ["/usr/bin/python", "-u", "/app/run-speedtest.py"]

