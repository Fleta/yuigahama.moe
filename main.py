from fastapi import FastAPI
from starlette.routing import Mount
from starlette.staticfiles import StaticFiles
from starlette.responses import HTMLResponse
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse, FileResponse

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

@app.get("/api/catbot/cat-image/{item_id}")
async def serve_cat_image(item_id):
    return FileResponse("./static/images/cats/" + item_id, media_type="image/jpg")


@app.post("/api/catbot/simple-text-response")
async def simple_text_response(message: dict):
    # logger.debug(jsonable_encoder(kakao_request.Request(**message)))
    response_data = {
        'status': 200,
        'response': response.say_hello()
    }
    return JSONResponse(content=jsonable_encoder(
        normal_response.Response(**response_data)) 
        # kakao_response.Reponse(**response_data)
    )

@app.post("/api/catbot/simple-image-response")
async def simple_image_response(message: dict):
    return response.serve_sample_image("https://placekitten.com/200/300", "sample cat image")

@app.post("/api/catbot/call-cat")
async def call_cat_response(message: dict):
    data = jsonable_encoder(kakao_request.Request(**message)).get('data')
    return response.serve_cat_image("", "당신이 찾는 고양이")