FROM centos:7
MAINTAINER gboorse

##
## This Dockerfile creates the Videowatcher frontend
##

#add packages
RUN yum -y install yum-utils wget which
RUN yum -y groupinstall development

#enable IUS
RUN yum -y install https://centos7.iuscommunity.org/ius-release.rpm

#install python
RUN yum -y install python35u

#install pip
RUN wget https://bootstrap.pypa.io/get-pip.py && python3.5 get-pip.py

#install virtualenv 
RUN pip install virtualenv

#create a user
RUN useradd vw_user 

#make the directory 
RUN mkdir -p /opt/videowatcher

#copy all of the files in
COPY . /opt/videowatcher

#set permissions
RUN chown -R vw_user /opt/videowatcher

#set working directory
WORKDIR /opt/videowatcher

#configure virtual environment
RUN ./setup.sh

#expose correct port
EXPOSE 5000

#set user
USER vw_user

#this is a python3 thing
ENV LANG en_US.utf8

#run the script!
CMD ["./run.sh"]