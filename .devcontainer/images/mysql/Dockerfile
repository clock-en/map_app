FROM mysql:8.0
ENV TZ=UTC
COPY ./mysqld.cnf /etc/mysql/mysql.conf.d/mysqld.cnf
COPY ./initdb.d /docker-entrypoint-initdb.d