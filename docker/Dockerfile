FROM node:0.10
MAINTAINER Alex Gonzalez <agonzalezro@gmail.com>

RUN npm install -g reveal-md

VOLUME ["/slides"]
WORKDIR /slides

EXPOSE 1948
CMD ["reveal-md", "--theme=simple"]
