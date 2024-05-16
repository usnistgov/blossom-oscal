# blossom-oscal
OSCAL content that supports the BloSS@M project.


## Using local git-actions with NEKTOS/ACT
- BASH is preferred by ACT as zsh has some known issues
- Specify DOCKER_HOST location for Rancher or other alternative containerization tool. It informs Nektos/ACT to use current DOCKER_HOST in non-Docker configuration on MacOS. Alternative OS Guidance can be found [here](https://nektosact.com/usage/custom_engine.html)
```
export DOCKER_HOST=$(docker context inspect --format '{{.Endpoints.docker.Host}}') 
```

- To list actions available:
  ```
  act -l
  ```
