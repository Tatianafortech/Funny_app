# Funny_app
funny_app


test 

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



-> webhooks:
https://www.blazemeter.com/blog/how-to-integrate-your-github-repository-to-your-jenkins-project


-> https://ngrok.com/docs/integrations/hostedhooks/webhooks/ 
brew install ngrok

-> status check - investigate - CREATE
https://stackoverflow.com/questions/14274293/show-current-state-of-jenkins-build-on-github-repo/51003334#51003334
https://www.youtube.com/watch?v=jSm0YZ-NQAc

![image](https://github.com/Tatianafortech/Funny_app/assets/111741943/25ce0eeb-46f9-408e-b258-fc582425e867)

![image](https://github.com/Tatianafortech/Funny_app/assets/111741943/147aa5b8-4c11-43a0-88db-f9ccbaf1100e)
