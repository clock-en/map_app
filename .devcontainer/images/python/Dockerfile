FROM python:3.9.13
WORKDIR /workspace
COPY requirements.txt .
RUN apt update && apt install -y vim git \
    && echo "source /usr/share/bash-completion/completions/git" >> ~/.bashrc \
    && pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt
COPY . /workspace