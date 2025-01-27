FROM python:3.12-bookworm

RUN tar xf /home/user/Downloads/allure-2.29.0.tgz -C /home/user/tools

WORKDIR /usr/workspace
COPY ./requirements.txt /usr/workspace
RUN pip install -r requirements.txt
RUN playwright install --with-deps
