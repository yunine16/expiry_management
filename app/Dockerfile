FROM python:3.6

ARG app_dir=/app/src/

ADD requirements.txt $app_dir

WORKDIR $app_dir

RUN pip install -r requirements.txt