# Funny_app
funny_app

# install system tools
Install rancher desktop -> websearch
brew install docker-credential-helper 

# start rancher desktop 
- uncheck Kubernetes  and wait to start (arround 30 secs)

# download locally Dokerfile 
-> in location execute command -> precontitions installed on docker 
docker build -t tatianagavrila/jenkins

# run container
docker run -v jenkins:/var/jenkins_home -p 8080:8080  tatianagavrila/jenkins:latest
- if not present it will doenload from remote repo from dokerhub
- in case of error run also:       docker context use rancher-desktop

# run jenkins image from:
http://127.0.0.1:8080/

