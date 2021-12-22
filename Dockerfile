FROM python:3.9-slim-buster as build-image

RUN apt-get update
RUN apt-get install tcpdump sqlite3 -y

ARG FUNCTION_DIR=/code
RUN mkdir -p ${FUNCTION_DIR}
WORKDIR ${FUNCTION_DIR}

COPY src/requirements.txt ${FUNCTION_DIR}/src/requirements.txt
RUN pip install -r src/requirements.txt

COPY . ${FUNCTION_DIR}
RUN mv ${FUNCTION_DIR}/config.json ${FUNCTION_DIR}/src

WORKDIR ${FUNCTION_DIR}/src
CMD python robo.py --config config.json
