FROM python:3.8-slim-buster
RUN apt-get -y update
ADD . /app
WORKDIR /Python-Pytest-with-Pytest-Selenium
RUN pip install -r requirements.txt
ADD entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

