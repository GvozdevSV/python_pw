FROM python:3.12-bookworm

# Устанавливаем необходимые зависимости для Allure
RUN apt-get update && \
    apt-get install -y curl unzip && \
    rm -rf /var/lib/apt/lists/*

# Устанавливаем Allure Commandline
RUN curl -o allure-2.24.0.tgz -Ls https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.24.0/allure-commandline-2.24.0.tgz && \
    tar -zxvf allure-2.24.0.tgz -C /opt/ && \
    ln -s /opt/allure-2.24.0/bin/allure /usr/bin/allure && \
    rm allure-2.24.0.tgz

WORKDIR /usr/workspace
COPY ./requirements.txt /usr/workspace
RUN pip install -r requirements.txt
RUN playwright install --with-deps
