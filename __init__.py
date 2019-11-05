from fastapi import FastAPI
from starlette.routing import Mount
from starlette.staticfiles import StaticFiles
from starlette.responses import HTMLResponse
from os import path

app = FastAPI()
app.mount('/static', StaticFiles(directory="static"), name="static")

@app.get("/")
async def read_root():
    with open("./static/index.html", "r") as html_file:
        return HTMLResponse(html_file.read(), status_code=200)