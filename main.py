from fastapi import FastAPI
from starlette.routing import Mount
from starlette.staticfiles import StaticFiles
from starlette.responses import HTMLResponse
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse

from os.path import abspath, dirname
import sys

sys.path.append(abspath(dirname(__file__) + "\\..\\"))
import bot_for_cat

app = FastAPI()
app.mount('/static', StaticFiles(directory="static"), name="static")

@app.get("/")
async def read_root():
    with open("./static/index.html", "r") as html_file:
        return HTMLResponse(html_file.read(), status_code=200)

@app.get("/resume")
async def resume_page():
    with open("./static/resume.html", "r", encoding="UTF8") as resume_file:
        return HTMLResponse(resume_file.read(), status_code=200)

@app.get("/api/catbot/test")
async def test_response():
    response_data = {
        'status': 200,
        'response': bot_for_cat.response.say_hello()
    }
    return JSONResponse(content=jsonable_encoder(
        bot_for_cat.models.normal_response.Response(**response_data)) 
    )