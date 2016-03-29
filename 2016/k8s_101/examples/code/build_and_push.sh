#!/bin/bash

function build_and_push {
  GOOS=linux go build
  docker build -t agonzalezro/$1 .
  rm -f $1
  docker push agonzalezro/$1
}

function build_and_push_current {
  build_and_push $(basename `pwd`)
}
