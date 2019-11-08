from fastapi import FastAPI
from starlette.routing import Mount
from starlette.staticfiles import StaticFiles
from starlette.responses import HTMLResponse
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse

from os.path import abspath, dirname
import sys, logging

sys.path.append(abspath(dirname(__file__) + "\\..\\"))
from bot_for_cat import response
from bot_for_cat.models import normal_response, kakao_request

app = FastAPI()
app.mount('/static', StaticFiles(directory="static"), name="static")

logger = logging.getLogger("app")
logger.setLevel(logging.DEBUG)

# fh = TimedRotatingFileHandler(filename = "./logs/yuigahama.moe.log", when="midnight", interval=1, encoding="UTF-8")
# fh.setLevel(logging.ERROR)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%ㅣ(levelname)s|%(filename)s:%(lineno)s] %(asctime)s >> %(message)s')
# fh.setFormatter(formatter)
ch.setFormatter(formatter)

# logger.addHandler(fh)
logger.addHandler(ch)

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
        'response': response.say_hello()
    }
    return JSONResponse(content=jsonable_encoder(
        normal_response.Response(**response_data)) 
    )

@app.post("/api/catbot/receive")
async def handle_receive_event(message: dict):
    logger.debug(jsonable_encoder(kakao_request.Request(**message)))
    response_data = {
        'status': 200,
        'response': response.say_hello()
    }
    return JSONResponse(content=jsonable_encoder(
        normal_response.Response(**response_data)) 
    )