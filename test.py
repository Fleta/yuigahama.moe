from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse
from os.path import abspath, dirname
import sys

sys.path.append(abspath(dirname(__file__) + "\\..\\"))
import bot_for_cat

request_data = {
  "intent": {
    "id": "fkrrb7ncaotxbqdmn7zcgfm4",
    "name": "블록 이름"
  },
  "userRequest": {
    "timezone": "Asia/Seoul",
    "params": {
      "ignoreMe": "true"
    },
    "block": {
      "id": "fkrrb7ncaotxbqdmn7zcgfm4",
      "name": "블록 이름"
    },
    "utterance": "발화 내용",
    "lang": "",
    "user": {
      "id": "788596",
      "type": "accountId",
      "properties": {}
    }
  },
  "bot": {
    "id": "5c8f25cb384c550f44a18e21",
    "name": "봇 이름"
  },
  "action": {
    "name": "0vkync0pzb",
    "clientExtra": "",
    "params": {},
    "id": "ccfqbgj1x9fgyb2lh5y86y4n",
    "detailParams": {}
  }
}

print(jsonable_encoder(
    bot_for_cat.models.kakao_request.Request(**request_data)) )

data = jsonable_encoder(bot_for_cat.models.kakao_request.Request(**request_data))
print(data['userRequest']['utterance'])
print('' in 'something')
print (abspath(dirname(__file__)))