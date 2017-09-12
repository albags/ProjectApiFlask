FROM mariadb:latest

COPY project_fda.sql /docker-entrypoint-initdb.d/project_fda.sql

ENV MYSQL_ALLOW_EMPTY_PASSWORD "yes" 
ENV MYSQL_RANDOM_ROOT_PASSWORD "no"
ENV MYSQL_ROOT_PASSWORD "mtb"
ENV MYSQL_USER  "root"
ENV MYSQL_PASSWORD "root"
ENV MYSQL_DATABASE "project_fda"

 
