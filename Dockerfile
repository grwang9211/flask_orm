#FROM hfs-dtr-dev.ntrs.com/hfs/nodebuildimage:v1 as builder
FROM ubuntu:18.04

# Create app directory
WORKDIR /flask

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

COPY ./requirements.txt /flask/requirements.txt

RUN pip3 install -r requirements.txt

COPY . /flask

RUN python3 manage.py  seed_db 

EXPOSE 8080

ENTRYPOINT [ "python3", "./wsgi.py" ]



