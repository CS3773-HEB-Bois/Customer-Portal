FROM openjdk:8-jdk-alpine

# Install sbt
RUN echo http://dl-cdn.alpinelinux.org/alpine/edge/testing \ 
  >> /etc/apk/repositories
RUN apk add --no-cache sbt

# Prepare Play env
ADD . /app
WORKDIR /app

ENTRYPOINT [ "./sbt", "run" ]