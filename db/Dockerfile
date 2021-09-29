FROM --platform=linux/amd64 mysql:8.0
EXPOSE 3306

ADD ./my.cnf /etc/db/conf.d/my.cnf

CMD ["mysqld"]