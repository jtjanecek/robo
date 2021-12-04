FROM python:3.9-slim-buster as build-image

RUN apt-get update
RUN apt-get install tcpdump -y

ARG FUNCTION_DIR=/code
RUN mkdir -p ${FUNCTION_DIR}
WORKDIR ${FUNCTION_DIR}
COPY . ${FUNCTION_DIR}

RUN mv ${FUNCTION_DIR}/config.json ${FUNCTION_DIR}/src

WORKDIR ${FUNCTION_DIR}/src

RUN pip install -r requirements.txt

CMD python robo.py --config config.json
