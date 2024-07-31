from fastapi import FastAPI, Request, Response
from slack_bolt import App
from slack_bolt.adapter.fastapi import SlackRequestHandler
from .slack_app import  app as slack_app
api = FastAPI(prefix="/slack", tags=["slack"], )

handler = SlackRequestHandler(app=slack_app)

@api.get("/")
def index():
    return {"Hello": "World"}

@api.post("/slack/events")
async def slack_endpoint(req: Request):
    return await handler.handle(req)


@api.post("/slack/actions")
async def slack_action_endpoint(req: Request):
    return await handler.handle(req)