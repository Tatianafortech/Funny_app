FROM docker.io/jenkins/jenkins:lts

USER root
RUN apt-get update
RUN apt-get install -y ca-certificates curl apt-transport-https apt-utils software-properties-common make gnupg2
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -
RUN add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable"
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y docker.io
RUN apt-get install -y python3
RUN ln -s /usr/bin/python3 /usr/bin/python
RUN ln -s /usr/bin/python3

RUN apt-get install -y python3 python3-pip python3-venv python3-pytest
#RUN apt-get install -y python3-flask-script

RUN ln -s /usr/bin/python3-pip /usr/bin/python-pip
RUN ln -s /usr/bin/python3-pytest /usr/bin/python-pytest
RUN  apt-get install -y python3-flask


RUN apt-get -y upgrade 

#RUN pip install flask

#RUN apt-get install Flask

RUN usermod -aG docker jenkins



# local issue
RUN find /var/run -gid 999 -exec chgrp -v 996 '{}' \;
# end local issue

RUN chown -R jenkins:jenkins /var/jenkins_home

VOLUME [ "/var/jenkins_home" ]

USER jenkins
#RUN  sudo python3 -m venv venv
#RUN  . venv/bin/activate