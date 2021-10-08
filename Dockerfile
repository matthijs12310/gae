FROM ubuntu:18.04

CMD docker run -it --init -p 8080:8080 -v "$(pwd):/home/workspace:cached" gitpod/openvscode-server