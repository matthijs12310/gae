FROM ubuntu:18.04

CMD dpkg -i docker-ce_20.10.9_3-0_ubuntu-bionic_arm64.deb
RUN docker run -it --init -p 8080:8080 -v "$(pwd):/home/workspace:cached" gitpod/openvscode-server