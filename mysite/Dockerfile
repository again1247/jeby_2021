# This shows systemd services (nginx and named) running in a centos7 container.
# There have been lots of problems and workarounds for this, see:
# https://hub.docker.com/_/centos/
# https://github.com/docker/docker/issues/7459

FROM centos:centos7

RUN yum install -y epel-release # for nginx
RUN yum install -y initscripts  # for old "service"

ENV container=docker

RUN (cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == systemd-tmpfiles-setup.service ] || rm -f $i; done); \
rm -f /lib/systemd/system/multi-user.target.wants/*;\
rm -f /etc/systemd/system/*.wants/*;\
rm -f /lib/systemd/system/local-fs.target.wants/*; \
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \
rm -f /lib/systemd/system/basic.target.wants/*;\
rm -f /lib/systemd/system/anaconda.target.wants/*;

# named (dns server) service
RUN yum install -y bind bind-utils
RUN systemctl enable named.service 
