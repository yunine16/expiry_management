FROM python:3.6

ARG app_dir=/app/src/

ADD requirements.txt $app_dir

WORKDIR $app_dir

RUN pip install -r requirements.txt

RUN apt-get install -y cron

ADD python-cron /etc/cron.d/python-cron

RUN chmod 0644 /etc/cron.d/python-cron

RUN chmod +x /script.sh /init.sh

CMD /init.sh