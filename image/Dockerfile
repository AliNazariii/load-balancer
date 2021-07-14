FROM python:3.8-slim

ENV DockerHome=/home

COPY requirements.txt ${DockerHome}

WORKDIR ${DockerHome}

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . ${DockerHome}

EXPOSE 50051

CMD cd ${DockerHome} && python server.py