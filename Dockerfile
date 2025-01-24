FROM python:3.12-bookworm

WORKDIR /usr/workspace
COPY ./requirements.txt /usr/workspace
RUN pip install -r requirements.txt
RUN playwright install --with-deps
