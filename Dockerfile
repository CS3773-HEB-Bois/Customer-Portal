FROM openjdk:8-jdk-alpine

# Install bash
RUN apk update && apk add bash

# Install sbt
RUN apk update && apk add bash
RUN echo http://dl-cdn.alpinelinux.org/alpine/edge/testing \ 
  >> /etc/apk/repositories
RUN apk add --no-cache sbt

# Prepare Play env
ADD . /app
WORKDIR /app

ENTRYPOINT [ "sbt", "run" ]
