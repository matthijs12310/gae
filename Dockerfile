FROM ubuntu:18.04

RUN docker run -it --init -p 8080:8080 -v "$(pwd):/home/workspace:cached" gitpod/openvscode-server