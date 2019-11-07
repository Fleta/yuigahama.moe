# yuigahama.moe-main

API and WEB server for personal blog and other services, visit [my page](https://yuigahama.moe)

## installation

```
pip install -r requirements.txt
```

or 

```
python3 -m pip install -r requirements.txt
```

or 

```
pip3 install -r requirements.txt
```

## run

```
uvicorn main:app --reload
```

or

```
python -m uvicorn main:app --reload
```

`main`: `main.py`, the main script of project

`app`: the object created inside of main script with the line `app = FastAPI()`.

`--reload`: make the server restart after code changes. Only do this for development.