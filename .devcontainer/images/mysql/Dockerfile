FROM mysql:8.0
ENV TZ=UTC
COPY ./my.cnf /etc/mysql/conf.d/my.cnf
COPY ./initdb.d /docker-entrypoint-initdb.d