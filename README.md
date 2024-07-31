# AWESOME MicroService 

What is the Awesome Microservice? 
Well really I'm not sure yet, I think it will be a combination of micro services that
I find to be useful to me.

## Roadmap? 

- Authentication Service
- Career Compass
- React Frontend
- Slack Application Bot


## Microservices

### Career Compass

CRUD application for handling tracking daily, weekly, and monthly completed tasks and projects
This data will be collected and used to build resume, promotion documentation, and more. 
But will start simple for tracking tasks with a web frontend, and a slack intergration. 


### Slack API

Simple slack bot to interact with the microservices being developed and deployed. 

```bash
export SLACK_BOT_TOKEN=xoxb-XXXXXXXXXXXXXXXXX
export SLACK_SIGNING_SECRET=XXXXXXXXXXXXXXXXX
```

## Deployment

Deploying the microservices we will use Docker and Docker compose to deploy the services. 
Using Traefik as a reverse proxy for the api