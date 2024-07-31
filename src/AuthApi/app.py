from fastapi import FastAPI

app = FastAPI()

@app.get("/token")
def get_access_token():
    return {"token": "<PASSWORD>"}