#!/bin/bash

docker build --rm -t "seed:latest" seed_container && \
docker build --rm -t "simple:latest" simple_pipeline_container && \
docker build --rm -t "java_build:latest" java_build_container

 
