from fastapi import FastAPI

from .adapters.input.controllers.account_controller import AccountController

app = FastAPI()

app.include_router(AccountController().router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
